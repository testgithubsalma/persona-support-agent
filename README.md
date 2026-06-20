# Persona Adaptive Customer Support Agent 🤖

## Project Overview

The Persona Adaptive Customer Support Agent is an AI-powered support system designed to provide personalized customer interactions by identifying customer personas and adapting responses accordingly.

The system analyzes user queries, detects the customer's persona, retrieves relevant support information from a knowledge base, generates persona-specific responses, and escalates complex issues to a human support representative when necessary.

---

## Supported Customer Personas

### Technical Expert

* Uses technical terminology and domain-specific language.
* Requests logs, configurations, APIs, and troubleshooting details.
* Prefers detailed and technical explanations.

### Frustrated User

* Expresses dissatisfaction or urgency.
* Reports repeated failures or unresolved issues.
* Requires empathetic and reassuring communication.

### Business Executive

* Focuses on business impact and outcomes.
* Prefers concise and professional responses.
* Interested in resolution timelines and operational impact.

---

## Key Features

* Persona Detection
* Adaptive Response Generation
* Knowledge Base Retrieval
* Human Escalation Workflow
* Handoff Summary Generation
* Streamlit-Based User Interface
* Gemini AI Integration

---

## Project Structure

```text
persona-support-agent/

├── app.py
├── requirements.txt
├── README.md

├── data/
│   ├── account_security.md
│   ├── api_authentication.md
│   ├── billing_faq.txt
│   ├── cloud_setup.md
│   ├── database_troubleshooting.md
│   ├── password_reset.txt
│   ├── payment_gateway.md
│   ├── refund_policy.txt
│   └── user_management.md

├── src/
│   ├── __init__.py
│   ├── classifier.py
│   ├── rag_pipeline.py
│   ├── generator.py
│   ├── escalator.py
│   └── config.py
```

---

## Technology Stack

| Component                | Technology    |
| ------------------------ | ------------- |
| Programming Language     | Python 3.13   |
| User Interface           | Streamlit     |
| AI Model                 | Google Gemini |
| Configuration Management | Python Dotenv |
| Version Control          | Git & GitHub  |

---

## System Architecture

```text
User Query
     ↓
Persona Detection
     ↓
Knowledge Retrieval
     ↓
Response Generation
     ↓
Escalation Check
     ↓
Human Handoff Summary
```

---

## Escalation Conditions

The system escalates conversations to a human support representative when:

* Billing-related issues are reported.
* Refund requests are submitted.
* Legal or compliance concerns are raised.
* Sensitive account-related actions are required.
* The issue cannot be resolved automatically.

---

## Sample Queries

### Technical Expert

Can you explain the API authentication failure and provide error logs?

### Frustrated User

I have tried everything and nothing works. I am extremely frustrated.

### Business Executive

How does this issue impact business operations and when will it be resolved?

### Escalation Scenario

I need a refund because I was charged twice.

---

## Installation and Setup

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file in the project root directory:

```env
GEMINI_API_KEY=YOUR_API_KEY
```

### Run Application

```bash
streamlit run app.py
```

---

## Future Enhancements

* FAISS-Based Vector Search
* ChromaDB Integration
* Advanced Retrieval-Augmented Generation (RAG)
* Conversation Memory
* LangGraph Workflow Automation
* Sentiment Analysis
* Analytics Dashboard
* Human Approval Workflow

---

## Author

**Salma**

B.Tech – Computer Science and Engineering
