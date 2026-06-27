from email.message import EmailMessage
import base64


def send_reply(gmail_service, email, message_text):
    try:
        # יצירת מייל
        msg = EmailMessage()
        msg["To"] = extract_email(email["sender"])
        msg["Subject"] = "Re: " + email.get("subject", "")
        msg.set_content(message_text)

        # קידוד לפי Gmail API
        raw = base64.urlsafe_b64encode(msg.as_bytes()).decode()

        # שליחה
        gmail_service.users().messages().send(
            userId="me",
            body={"raw": raw}
        ).execute()

        print("📨 Reply sent successfully")

    except Exception as e:
        print("❌ Failed to send reply:", e)


def extract_email(sender_string: str):
    """
    מחלץ אימייל מתוך פורמט כמו:
    'Name <email@gmail.com>'
    """
    if "<" in sender_string and ">" in sender_string:
        return sender_string.split("<")[1].split(">")[0]
    return sender_string