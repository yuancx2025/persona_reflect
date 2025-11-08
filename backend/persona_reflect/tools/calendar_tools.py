from datetime import datetime, timedelta
from typing import List, Dict, Any
from pydantic import BaseModel
from services.gcal_demo import suggest_slots as g_suggest, create_block as g_create


class CalendarEvent(BaseModel):
    """Data model representing a single calendar event"""

    title: str
    description: str
    start_time: datetime
    duration_minutes: int = 30
    priority: str = "medium"  # could be "low", "medium", or "high"


class CalendarTool:
    """
    Calendar tool that wraps both local and Google Calendar functionality.
    The external interface (methods) stays the same, but internally this class
    now delegates scheduling to the real Google Calendar API for demo purposes.
    """

    def __init__(self):
        # Keep local storage for mock or fallback
        self.events: List[CalendarEvent] = []

    def suggest_time_slots(
        self,
        duration_minutes: int = 30,
        days_ahead: int = 7,
        preferred_hours: tuple = (9, 18),
    ) -> List[Dict[str, Any]]:
        """
        Suggest available time slots using Google Calendar free/busy data.
        If Google Calendar is connected, this returns real free time slots.
        """
        # Use the real Google FreeBusy API through g_suggest
        slots = g_suggest(
            days=days_ahead,
            duration=duration_minutes,
            work_hours=preferred_hours,
            topk=5,
        )
        # Convert the Google slot format to match the original mock tool output
        return [
            {
                "date": s["start"][:10],
                "time": s["start"][11:16],
                "datetime": s["start"],
                "label": s["label"],
            }
            for s in slots
        ]

    def create_event(self, event: CalendarEvent) -> Dict[str, Any]:
        """
        Create a real Google Calendar event based on the provided data.
        Still stores a local copy for displaying or offline fallback.
        """
        # Send event creation request to Google Calendar
        created = g_create(
            title=event.title,
            start_iso=event.start_time.isoformat(),
            duration=event.duration_minutes,
            description=event.description,
        )
        # Also store a local record for get_upcoming_events()
        self.events.append(event)

        return {
            "success": True,
            "event_id": created.get("id"),
            "message": f"Scheduled: {event.title} at {event.start_time.strftime('%Y-%m-%d %H:%M')}",
            "htmlLink": created.get("htmlLink"),
        }

    def get_upcoming_events(self, days: int = 7) -> List[Dict[str, Any]]:
        """
        Retrieve upcoming events from local memory.
        For a full implementation, this could query Google Calendar’s 'list' API instead.
        """
        now = datetime.now()
        cutoff = now + timedelta(days=days)

        upcoming = [
            {
                "title": e.title,
                "start_time": e.start_time.isoformat(),
                "duration": e.duration_minutes,
                "priority": e.priority,
            }
            for e in self.events
            if now <= e.start_time <= cutoff
        ]
        # Sort by chronological order
        return sorted(upcoming, key=lambda x: x["start_time"])
