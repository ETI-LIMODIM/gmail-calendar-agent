# gmail-calendar-agent
AI Agent for Gmail and Google Calendar

## מה הפרויקט עושה
זהו סוכן אוטומטי (AI Agent) שמנהל מיילים ולוח שנה באופן חכם:
- קורא מיילים מ-Gmail
- מזהה בקשות לפגישות
- מנתח את תוכן המייל באמצעות AI
- בודק זמינות ביומן Google Calendar
- יוצר אירועים אוטומטיים
- שולח תשובות אוטומטיות

## טכנולוגיות
- Python
- Gmail API
- Google Calendar API
- Google OAuth2
- AI parsing logic
## איך מריצים את הפרויקט:
מתקינים ספריות: pip install -r requirements.txt  ומריצים python main.py

## מבנה הפרוייקט:

- `main.py` → הרצת הסוכן
- `gmail.py` → קריאת מיילים
- `calendar_service.py` → ניהול יומן
- `ai.py` → ניתוח תוכן
- `responder.py` → שליחת תשובות
- `auth.py` → התחברות ל-Google APIs
- `docs/` → תיעוד הפרויקט

## הערות חשובות
- קבצים רגישים (token.json, credentials.json) לא כלולים ב-GitHub
- זה פרויקט לימודי המדמה סוכן אוטומטי אמיתי

<img width="1892" height="985" alt="image" src="https://github.com/user-attachments/assets/725bc55a-9362-4a02-8c69-1e38e8b26b0d" />


