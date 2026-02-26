RULES = {
    "promotion": {
        "default_action": "Later"
    },
    "alert": {
        "default_action": "Now"
    }
}

def get_rule(event_type):
    return RULES.get(event_type, {
        "default_action": "Now"
    })