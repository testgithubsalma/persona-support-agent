def detect_persona(query):
    query = query.lower()

    if any(word in query for word in [
        "api", "database", "error", "log",
        "configuration", "authentication"
    ]):
        return "Technical Expert"

    elif any(word in query for word in [
        "frustrated", "angry", "nothing works",
        "tried everything", "annoyed"
    ]):
        return "Frustrated User"

    return "Business Executive"