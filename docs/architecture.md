# 🏗️ SupportFlow AI — System Architecture

This document describes the architecture of **SupportFlow AI**, a production-inspired multi-agent customer support platform built with **CrewAI**, **Google Gemini**, **Pinecone RAG**, **FastAPI**, **SQLite**, and **Streamlit**.

---

# 📖 Architecture Overview

SupportFlow AI follows a modular architecture where each layer has a single responsibility.

The application consists of:

* Frontend Dashboard
* FastAPI Backend
* Multi-Agent AI Layer
* Retrieval-Augmented Generation (RAG)
* SQLite Database
* Pinecone Vector Database
* Google Gemini LLM

This separation makes the system easier to maintain, extend, and deploy.

---

# 🏛 High-Level Architecture

> Replace the image below with your generated architecture diagram.

```markdown
<img src="frontend/assets/architecture-diagram.png" width="100%">
```

---

# 🖥 Frontend Layer

Technology:

* Streamlit
* Plotly
* Pandas

Responsibilities:

* Submit customer support requests
* Display AI-generated responses
* View ticket history
* Search previous tickets
* Display analytics dashboards

The frontend communicates exclusively with the FastAPI backend through REST APIs.

---

# ⚙️ Backend Layer

Technology:

* FastAPI
* SQLAlchemy
* Uvicorn

Responsibilities:

* Expose REST API endpoints
* Validate incoming requests
* Trigger the CrewAI workflow
* Store processed tickets
* Retrieve analytics
* Serve ticket history

The backend acts as the central orchestration layer between the UI, AI agents, and the database.

---

# 🤖 AI Orchestration Layer

Technology:

* CrewAI

SupportFlow AI uses multiple specialized AI agents instead of a single prompt.

Current agents:

### Intent Classification Agent

Responsibilities:

* Detect customer intent
* Identify category
* Determine priority
* Analyze sentiment

Outputs:

* Category
* Priority
* Sentiment

---

### Knowledge Retrieval Agent

Responsibilities:

* Query Pinecone
* Retrieve relevant company policies
* Build contextual knowledge for the LLM

Outputs:

* Relevant support documentation
* Context for response generation

---

### Response Generation Agent

Responsibilities:

* Generate professional customer responses
* Use retrieved knowledge
* Maintain consistent support tone

Outputs:

* Customer response

---

### Escalation Agent

Responsibilities:

* Decide if escalation is required
* Select the appropriate support team
* Explain the escalation reason

Outputs:

* Escalation status
* Assigned team
* Escalation reason

---

# 📚 Retrieval-Augmented Generation (RAG)

Technology:

* Pinecone Vector Database

Knowledge documents are stored inside:

```text
knowledge_base/
```

Examples:

* Billing Policy
* Login Help
* Refund Policy
* Security Policy
* Technical Policy

During every request:

1. Customer query is embedded.
2. Pinecone performs similarity search.
3. Relevant documents are retrieved.
4. Context is injected into Gemini.
5. Gemini generates an informed response.

This approach significantly reduces hallucinations by grounding responses in company-specific knowledge.

---

# 🧠 Large Language Model

Technology:

* Google Gemini

Gemini is responsible for:

* Understanding customer requests
* Reasoning over retrieved context
* Generating professional support responses

The architecture is modular and can be adapted to alternative LLM providers such as:

* OpenAI GPT
* Anthropic Claude
* Groq
* Ollama
* Azure OpenAI

---

# 🗄 Database Layer

Technology:

* SQLite
* SQLAlchemy ORM

Stored information includes:

* Ticket ID
* Customer message
* Category
* Priority
* Sentiment
* AI response
* Escalation status
* Assigned team
* Timestamp

SQLite is used for local development and demonstration purposes.

The persistence layer can be migrated to PostgreSQL or MySQL with minimal changes.

---

# 🔄 End-to-End Request Flow

```text
Customer Request
        │
        ▼
FastAPI API
        │
        ▼
CrewAI Orchestrator
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
Escalation Agent
        │
        ▼
SQLite Database
        │
        ▼
Streamlit Dashboard
```

---

# 📊 Scalability Considerations

The architecture has been designed with modularity in mind.

Potential production enhancements include:

* PostgreSQL instead of SQLite
* Redis caching
* Docker containers
* Kubernetes deployment
* Authentication and authorization
* CI/CD pipelines
* Monitoring with Prometheus and Grafana

---

# 📌 Summary

SupportFlow AI demonstrates how multiple AI agents can collaborate with Retrieval-Augmented Generation to automate customer support workflows.

By separating responsibilities across the frontend, backend, AI orchestration, knowledge retrieval, and persistence layers, the system remains maintainable, scalable, and easy to extend for future enhancements.
