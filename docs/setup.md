 # 🚀 SupportFlow AI — Setup Guide

This guide explains how to install and run **SupportFlow AI** on your local machine.

SupportFlow AI is a production-inspired **multi-agent customer support platform** powered by **CrewAI**, **Google Gemini**, **Pinecone RAG**, **FastAPI**, and **Streamlit**.

---

# 📋 Prerequisites

Before you begin, ensure you have the following installed:

* Python 3.12 or later
* Git
* UV (Python package manager)

You'll also need accounts for:

* Google AI Studio (Gemini API)
* Pinecone

---

# 🤖 AI Model

The current implementation uses **Google Gemini** as the Large Language Model (LLM).

Required:

* Google Gemini API Key

> **Note**
>
> The AI layer has been designed to be modular. With minor code changes, SupportFlow AI can be adapted to use other LLM providers such as:
>
> * OpenAI GPT
> * Anthropic Claude
> * Groq
> * Ollama (Local LLMs)
> * Azure OpenAI

---

# 📥 Clone the Repository

```bash
git clone https://github.com/shyamusammy/supportflow-ai.git

cd supportflow-ai
```

---

# 📦 Install Dependencies

SupportFlow AI uses **uv** for dependency management.

Install all project dependencies:

```bash
uv sync
```

This installs every package defined in `pyproject.toml`.

---

# ⚙️ Configure Environment Variables

Copy the example environment file:

```bash
cp .env.example .env
```

or create a `.env` file manually.

Example configuration:

```env
GOOGLE_API_KEY=your_google_gemini_api_key

PINECONE_API_KEY=your_pinecone_api_key

PINECONE_INDEX=support-kb
```

> **Important**
>
> Never commit your `.env` file or API keys to GitHub.

---

# 📚 Prepare the Knowledge Base

SupportFlow AI uses **Retrieval-Augmented Generation (RAG)** to answer customer queries using company knowledge.

Knowledge documents are stored in:

```text
knowledge_base/
```

Example documents:

```text
knowledge_base/

├── billing_policy.txt
├── login_help.txt
├── refund_policy.txt
├── security_policy.txt
├── subscription_policy.txt
└── technical_policy.txt
```

If you modify or add documents, rerun the ingestion process to update the Pinecone vector database.

---

# 🚀 Start the FastAPI Backend

Launch the backend server:

```bash
uv run uvicorn app.api.main:app --reload
```

FastAPI will be available at:

```text
http://127.0.0.1:8000
```

Swagger Documentation:

```text
http://127.0.0.1:8000/docs
```

---

# 🖥️ Start the Streamlit Dashboard

Open a **new terminal**.

Run:

```bash
uv run streamlit run frontend/app.py
```

The dashboard will be available at:

```text
http://localhost:8501
```

---

# ✅ Verify the Installation

Once both services are running:

### FastAPI

Open:

```text
http://127.0.0.1:8000/docs
```

You should see the Swagger API documentation.

---

### Streamlit

Open:

```text
http://localhost:8501
```

You should see the **SupportFlow AI** dashboard with the following pages:

* 🤖 About
* 📊 Dashboard
* 🎫 Ticket History
* 📈 Analytics

---

# 📁 Project Structure

```text
supportflow-ai/

├── app/
│   ├── agents/
│   ├── api/
│   ├── database/
│   ├── repositories/
│   ├── routers/
│   ├── services/
│   ├── tasks/
│   └── utils/
│
├── frontend/
│   ├── assets/
│   ├── pages/
│   └── services/
│
├── knowledge_base/
│
├── docs/
│
├── README.md
├── LICENSE
├── pyproject.toml
├── uv.lock
└── .env.example
```

---

# 🔧 Troubleshooting

## Missing Dependencies

If dependencies are missing:

```bash
uv sync
```

---

## Streamlit Cannot Connect to FastAPI

Ensure the backend is running before starting the frontend.

Backend:

```bash
uv run uvicorn app.api.main:app --reload
```

Frontend:

```bash
uv run streamlit run frontend/app.py
```

---

## Pinecone Connection Issues

Verify:

* Pinecone API Key
* Pinecone Index Name
* Internet Connection

---

## Google Gemini Authentication Issues

Check:

* Your Gemini API Key is valid.
* The key is correctly added to your `.env` file.
* Your Google AI Studio project has API access enabled.

---

# 🔄 Customizing the LLM

SupportFlow AI currently integrates with **Google Gemini**.

Because the AI layer is modular, developers can replace Gemini with another LLM provider.

Typical changes include:

* Updating the LLM client configuration
* Modifying agent initialization
* Replacing API keys
* Updating environment variables
* Adjusting model-specific parameters

Supported alternatives include:

* OpenAI GPT
* Anthropic Claude
* Groq
* Ollama
* Azure OpenAI

---

# 🗄️ Database

The project currently uses **SQLite** for local development and demonstration.

For production deployments, the persistence layer can be migrated to:

* PostgreSQL
* MySQL
* Microsoft SQL Server

with minimal changes to the SQLAlchemy configuration.

---

# 🎉 You're Ready!

If everything has been configured successfully:

* ✅ FastAPI is running
* ✅ Streamlit is running
* ✅ Pinecone is connected
* ✅ Google Gemini is configured

You can now submit customer support requests, retrieve AI-generated responses, explore ticket history, and monitor analytics through the SupportFlow AI dashboard.
