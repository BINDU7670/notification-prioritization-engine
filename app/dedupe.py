# Simple in-memory store (demo purpose only)
recent_events = set()

def is_duplicate(event):
    key = f"{event.user_id}:{event.dedupe_key or event.message}"
    if key in recent_events:
        return True
    recent_events.add(key)
    return False