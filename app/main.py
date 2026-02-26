from fastapi import FastAPI
from .models import NotificationEvent
from .dedupe import is_duplicate
from .decision_engine import decide

app = FastAPI(title="Notification Prioritization Engine")

@app.post("/evaluate")
def evaluate(event: NotificationEvent):
    duplicate = is_duplicate(event)
    decision, reason = decide(event, duplicate)

    return {
        "decision": decision,
        "reason": reason
    }