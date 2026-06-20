import streamlit as st
from google import genai

client = genai.Client(api_key="AQ.Ab8RN6IBd5DFPEF9-Oj1aBI0uww9lEXP5BWx4dPeUl9LaXUAbQ")

st.title("Persona Adaptive Support Agent")

message = st.text_area("Customer Message")

if st.button("Submit"):

    if "api" in message.lower() or "error" in message.lower():
        persona = "Technical Expert"

    elif "frustrated" in message.lower() or "angry" in message.lower() or "nothing works" in message.lower():
        persona = "Frustrated User"

    else:
        persona = "Business Executive"

    prompt = f"""
Persona: {persona}

User Message:
{message}

Respond in the style of that persona.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    st.write("Detected Persona:")
    st.success(persona)

    st.write("Response:")
    st.write(response.text)

    if "billing" in message.lower() or "legal" in message.lower():
        st.error("Escalated To Human Agent")

        st.json({
            "persona": persona,
            "issue": message,
            "recommendation": "Human review required"
        })