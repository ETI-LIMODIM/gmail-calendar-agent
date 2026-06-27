import time
import json
from googleapiclient.discovery import build

from gmail import get_unread_emails
from ai import analyze_email
from calendar_service import check_availability, create_event
from responder import send_reply
from auth import get_credentials


MEMORY_FILE = "memory.json"


def load_memory():
    try:
        with open(MEMORY_FILE, "r") as f:
            return set(json.load(f))
    except:
        return set()


def save_memory(memory):
    with open(MEMORY_FILE, "w") as f:
        json.dump(list(memory), f)


def run():
    creds = get_credentials()

    gmail = build("gmail", "v1", credentials=creds)
    calendar = build("calendar", "v3", credentials=creds)

    processed = load_memory()

    print("🚀 Agent started...")

    while True:
        emails = get_unread_emails(gmail)

        for email in emails:

            if email["id"] in processed:
                continue

            print(f"\n📩 New email: {email['subject']}")

            analysis = analyze_email(email["body"])

            if analysis["type"] == "meeting_request":

                start = analysis["start"]
                end = analysis["end"]

                if check_availability(calendar, start, end):

                    event_id = create_event(calendar, email, analysis)

                    send_reply(
                        gmail,
                        email,
                        f"נקבעה פגישה ✔ ({event_id})"
                    )

                    print("📅 Meeting created")

                else:

                    send_reply(
                        gmail,
                        email,
                        "לא פנוי בזמן המבוקש — נציע חלופות"
                    )

                    print("⛔ Not available")

            else:
                print("📭 Not a meeting request")

            processed.add(email["id"])

        save_memory(processed)

        time.sleep(60)


if __name__ == "__main__":
    run()