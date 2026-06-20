def generate_response(persona, query):

    if persona == "Technical Expert":
        return f"""
Technical Analysis:

Issue: {query}

Possible Causes:
1. Authentication failure
2. Configuration mismatch
3. Invalid API credentials

Recommended Troubleshooting:
- Verify API key
- Check logs
- Validate configuration
"""

    elif persona == "Frustrated User":
        return f"""
I understand your frustration.

Issue: {query}

Please don't worry. Let's resolve this step by step.

Recommended Action:
- Verify account settings
- Retry the process
- Contact support if the issue persists
"""

    else:
        return f"""
Business Summary

Issue: {query}

Business Impact:
Potential impact on productivity and operations.

Recommendation:
Investigate promptly and monitor service availability.
"""