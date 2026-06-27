import re

MEETING_KEYWORDS = [
    "פגישה", "meeting", "schedule", "call",
    "zoom", "meet", "appointment",
    "לקבוע", "זמן", "available", "calendar"
]

TIME_PATTERN = r"(\d{1,2}:\d{2})"


def analyze_email(text: str):
    if not text:
        return {"type": "other"}

    text_lower = text.lower()

    # זיהוי פגישה
    is_meeting = any(word in text_lower for word in MEETING_KEYWORDS)

    if not is_meeting:
        return {"type": "other"}

    # ניסיון חילוץ שעה
    match = re.search(TIME_PATTERN, text_lower)

    if match:
        hour, minute = map(int, match.group(1).split(":"))
    else:
        hour, minute = 15, 0  # ברירת מחדל

    from datetime import datetime, timedelta

    start = datetime.now().replace(hour=hour, minute=minute, second=0, microsecond=0)
    end = start + timedelta(hours=1)

    return {
        "type": "meeting_request",
        "start": start,
        "end": end
    }