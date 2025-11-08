# services/gcal_demo.py
import os, json
from datetime import datetime, timedelta
from typing import List, Dict, Optional
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

SCOPES = [os.getenv("GOOGLE_CALENDAR_SCOPES", "https://www.googleapis.com/auth/calendar")]
TOKEN_PATH = ".gcal_token.json"
CREDENTIALS_FILE = "credentials.json"
USER_TZ = os.getenv("GOOGLE_CALENDAR_TIMEZONE", "UTC")

def _authorize():
    creds = None
    if os.path.exists(TOKEN_PATH):
        creds = Credentials.from_authorized_user_file(TOKEN_PATH, SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, SCOPES)
            creds = flow.run_local_server(port=0) 
        with open(TOKEN_PATH, "w") as f:
            f.write(creds.to_json())
    return build("calendar", "v3", credentials=creds)

svc = None
def gcal():
    global svc
    if not svc:
        svc = _authorize()
    return svc

def suggest_slots(days=3, duration=60, work_hours=(9,18), topk=3) -> List[Dict]:
    now = datetime.now()
    start = (now + timedelta(days=1)).replace(hour=work_hours[0], minute=0, second=0, microsecond=0)
    end   = (now + timedelta(days=days)).replace(hour=work_hours[1], minute=0, second=0, microsecond=0)

    fb = gcal().freebusy().query(body={
        "timeMin": start.isoformat()+"Z",
        "timeMax": end.isoformat()+"Z",
        "items": [{"id": "primary"}],
        "timeZone": USER_TZ,
    }).execute()
    busy = fb["calendars"]["primary"].get("busy", [])

    gran = 30
    slots, cursor = [], start
    def overlaps(a,b):
        return not (a[1] <= b[0] or a[0] >= b[1])

    while cursor + timedelta(minutes=duration) <= end and len(slots) < topk:
        block_end = cursor + timedelta(minutes=duration)
        conflict = False
        for b in busy:
            bs = datetime.fromisoformat(b["start"].replace("Z","+00:00"))
            be = datetime.fromisoformat(b["end"].replace("Z","+00:00"))
            if overlaps((cursor, block_end), (bs, be)):
                conflict = True
                cursor = min(block_end, be)  
                break
        if not conflict:
            slots.append({
                "start": cursor.isoformat(),
                "end": block_end.isoformat(),
                "label": cursor.strftime("%a %m/%d %H:%M")
            })
            cursor = block_end + timedelta(minutes=gran) 
    return slots

def create_block(title:str, start_iso:str, duration:int=60, description:str="") -> Dict:
    start = datetime.fromisoformat(start_iso)
    end = start + timedelta(minutes=duration)
    body = {
        "summary": title,
        "description": description,
        "start": {"dateTime": start.isoformat(), "timeZone": USER_TZ},
        "end":   {"dateTime": end.isoformat(),   "timeZone": USER_TZ},
    }
    created = gcal().events().insert(calendarId="primary", body=body, sendUpdates="all").execute()
    return {"id": created.get("id"), "htmlLink": created.get("htmlLink")}
