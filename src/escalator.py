from src.config import ESCALATION_KEYWORDS

def should_escalate(query):

    query = query.lower()

    for keyword in ESCALATION_KEYWORDS:
        if keyword in query:
            return True

    return False


def generate_handoff(persona, query):

    return {
        "persona": persona,
        "issue": query,
        "documents_used": ["billing_policy.txt"],
        "attempted_steps": ["Automated response provided"],
        "recommendation": "Human agent review required"
    }