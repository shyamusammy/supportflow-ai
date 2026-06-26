# 🔄 SupportFlow AI — Workflow

This document describes the end-to-end workflow of **SupportFlow AI**, from the moment a customer submits a request until the ticket is processed, stored, and displayed in the analytics dashboard.

---

# 📖 Workflow Overview

SupportFlow AI uses a **CrewAI sequential workflow** to automate customer support operations.

Each AI agent is responsible for a specific task, allowing the system to produce consistent, context-aware responses while maintaining a modular architecture.

---

# 🧠 Workflow Diagram

> Replace the image below with your generated workflow diagram.

<img src="../frontend/assets/workflow-diagram.png" width="100%">

---

# 🚀 End-to-End Workflow

```text
Customer Request
        │
        ▼
FastAPI API
        │
        ▼
CrewAI Multi-Agent System
        │
        ▼
Intent Classification Agent
        │
        ▼
Knowledge Retrieval Agent
        │
        ▼
Pinecone Vector Search
        │
        ▼
Google Gemini
        │
        ▼
Response Generation Agent
        │
        ▼
Escalation Decision Agent
        │
        ▼
SQLite Database
        │
        ▼
Streamlit Dashboard
```

---

# Step 1 — Customer Request

The workflow begins when a customer submits a support request through:

* Streamlit Dashboard
* FastAPI REST API

Example:

```text
"I was charged twice for my subscription."
```

The request is forwarded to the FastAPI backend.

---

# Step 2 — FastAPI Processing

The backend:

* Receives the request
* Validates the input
* Generates a unique ticket ID
* Starts the CrewAI workflow

FastAPI acts as the entry point for all customer interactions.

---

# Step 3 — Intent Classification Agent

Responsibilities:

* Identify customer intent
* Determine ticket category
* Estimate ticket priority
* Analyze customer sentiment

Example Output:

| Field     | Value    |
| --------- | -------- |
| Category  | Billing  |
| Priority  | High     |
| Sentiment | Negative |

---

# Step 4 — Knowledge Retrieval Agent

The Knowledge Retrieval Agent performs **Retrieval-Augmented Generation (RAG)**.

Responsibilities:

* Convert the customer query into embeddings
* Search the Pinecone vector database
* Retrieve the most relevant support documentation

Example:

Customer asks:

```text
"I want a refund."
```

Retrieved knowledge:

* Refund Policy
* Billing Policy

The retrieved context is passed to the LLM.

---

# Step 5 — Google Gemini

Gemini receives:

* Customer request
* Intent analysis
* Retrieved company knowledge

Gemini generates a contextual and professional response grounded in the retrieved documents.

This significantly reduces hallucinations compared to prompting without retrieval.

---

# Step 6 — Response Generation Agent

Responsibilities:

* Format the AI response
* Ensure a professional customer support tone
* Include guidance based on company policies

Output:

* Customer response

---

# Step 7 — Escalation Decision Agent

Responsibilities:

* Decide whether human intervention is required
* Assign the appropriate support team
* Explain the escalation decision

Example:

| Field    | Value                       |
| -------- | --------------------------- |
| Escalate | Yes                         |
| Team     | Security Operations         |
| Reason   | Possible account compromise |

---

# Step 8 — Ticket Storage

After processing, the ticket is stored in SQLite.

Stored fields include:

* Ticket ID
* Customer message
* Category
* Priority
* Sentiment
* AI response
* Escalation status
* Assigned team
* Timestamp

The repository layer handles all database interactions.

---

# Step 9 — Dashboard Update

The Streamlit frontend retrieves ticket information through the FastAPI API.

Users can:

* View recent tickets
* Search ticket history
* Monitor analytics
* Review escalation trends

The dashboard reflects newly processed tickets without requiring manual database queries.

---

# Example Workflow

Customer Request:

```text
"I think someone hacked my account."
```

Processing Flow:

```text
Customer
        │
        ▼
Intent Classification
        │
        ▼
Category: Login
Priority: Critical
Sentiment: Anxious
        │
        ▼
Knowledge Retrieval
        │
        ▼
Security Policy
Login Help
        │
        ▼
Google Gemini
        │
        ▼
Generate Secure Response
        │
        ▼
Escalation Agent
        │
        ▼
Escalate = True
Assigned Team = Security Operations Center
        │
        ▼
SQLite
        │
        ▼
Dashboard
```

---

# Benefits of the Workflow

The multi-agent workflow provides several advantages over a single-prompt AI system:

* Separation of responsibilities
* Better maintainability
* Improved response quality
* Context-aware answers using RAG
* Consistent escalation decisions
* Easier future expansion with additional agents

---

# Summary

SupportFlow AI processes customer requests through a structured multi-agent workflow.

By combining CrewAI, Google Gemini, Pinecone RAG, FastAPI, and SQLite, the platform delivers intelligent customer support while maintaining a modular architecture that can be extended for future use cases.
