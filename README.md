## Persona Adaptive Customer Support Agent 🤖

## Overview 🔍

An AI-powered customer support agent that automatically detects customer personas, retrieves relevant support information, generates adaptive responses, and escalates complex issues to human support when necessary.

The system identifies different customer types and adjusts communication style accordingly to improve customer experience and support efficiency.

## Supported Personas 👥

### Technical Expert

* Uses technical terminology
* Requests logs, APIs, configurations
* Prefers detailed technical explanations

### Frustrated User

* Uses emotional language
* Reports repeated issues
* Requires empathetic and reassuring responses

### Business Executive

* Focuses on business impact
* Prefers concise communication
* Wants resolution timelines and outcomes

## Features 🚀

* Persona Detection
* Adaptive Response Generation
* Knowledge Base Integration
* Human Escalation Workflow
* Handoff Summary Generation
* Streamlit Web Interface
* Gemini AI Integration

## Project Structure 📁

persona-support-agent/

├── app.py

├── data/

│ ├── account_security.md

│ ├── api_authentication.md

│ ├── billing_faq.txt

│ ├── cloud_setup.md

│ ├── database_troubleshooting.md

│ ├── password_reset.txt

│ ├── payment_gateway.md

│ ├── refund_policy.txt

│ └── user_management.md

├── README.md

└── requirements.txt

## Tech Stack 🛠️

* Python 3.13
* Streamlit
* Google Gemini API
* Python Dotenv

## Architecture 🏗️

User Query

↓

Persona Detection

↓

Knowledge Retrieval

↓

Adaptive Response Generation

↓

Escalation Check

↓

Human Handoff Summary

## Escalation Conditions ⚠️

The system escalates conversations when:

* Billing-related issues
* Refund requests
* Legal concerns
* Sensitive account issues
* Unsupported requests

## Example Queries 💬

### Technical Expert

Can you explain the API authentication failure and provide error logs?

### Frustrated User

I have tried everything and nothing works. I am extremely frustrated.

### Business Executive

How does this issue impact business operations and when will it be resolved?

### Escalation Example

I need a refund because I was charged twice.

## Installation ⚙️

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
GEMINI_API_KEY=YOUR_API_KEY
```

Run:

```bash
streamlit run app.py
```

## Future Improvements 🔮

* FAISS / ChromaDB Integration
* Advanced RAG Pipeline
* Conversation Memory
* LangGraph Workflow
* Sentiment Analysis
* Analytics Dashboard

## Author 👩‍💻

Salma

B.Tech Computer Science Engineering

AI Engineering Assignment Submission
