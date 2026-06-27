import base64


def get_unread_emails(gmail_service):
    try:
        results = gmail_service.users().messages().list(
            userId="me",
            labelIds=["UNREAD"],
            maxResults=10
        ).execute()

        messages = results.get("messages", [])
        emails = []

        for msg in messages:
            full = gmail_service.users().messages().get(
                userId="me",
                id=msg["id"],
                format="full"
            ).execute()

            payload = full.get("payload", {})
            headers = payload.get("headers", [])

            subject = next((h["value"] for h in headers if h["name"] == "Subject"), "")
            sender = next((h["value"] for h in headers if h["name"] == "From"), "")

            body = ""

            emails.append({
                "id": msg["id"],
                "subject": subject,
                "sender": sender,
                "body": body
            })

        return emails

    except Exception as e:
        print("❌ Gmail error:", e)
        return []