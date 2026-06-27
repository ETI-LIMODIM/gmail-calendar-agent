def check_availability(calendar_service, start, end):
    events = calendar_service.events().list(
        calendarId="primary",
        timeMin=start.isoformat(),
        timeMax=end.isoformat(),
        singleEvents=True
    ).execute()

    return len(events.get("items", [])) == 0


def create_event(calendar_service, email, analysis):
    event = {
        "summary": f"Meeting with {email['sender']}",
        "start": {"dateTime": analysis["start"].isoformat(), "timeZone": "UTC"},
        "end": {"dateTime": analysis["end"].isoformat(), "timeZone": "UTC"},
    }

    created = calendar_service.events().insert(
        calendarId="primary",
        body=event
    ).execute()

    return created["id"]