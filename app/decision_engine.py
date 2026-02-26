from datetime import datetime
from .rule_engine import get_rule

def calculate_score(event):
    urgency = 0.9 if event.event_type == "alert" else 0.4
    return (0.6 * urgency) + (0.4 * event.priority_hint)

def decide(event, duplicate):
    if event.expires_at and event.expires_at < datetime.utcnow():
        return "Never", "Expired notification"

    if duplicate:
        return "Never", "Duplicate detected"

    rule = get_rule(event.event_type)
    score = calculate_score(event)

    if score >= 0.7:
        return "Now", f"High priority score: {score}"
    elif score >= 0.4:
        return "Later", f"Medium priority score: {score}"
    else:
        return "Never", f"Low priority score: {score}"