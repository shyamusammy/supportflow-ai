# 🚀 SupportFlow AI — Deployment Guide

This document describes how to deploy **SupportFlow AI** for development and production environments.

SupportFlow AI consists of two independent applications:

* **FastAPI Backend** – AI processing and REST API
* **Streamlit Frontend** – User interface and analytics dashboard

Separating the frontend and backend allows each service to scale independently.

---

# Deployment Overview

```text
                 User
                  │
                  ▼
        Streamlit Dashboard
                  │
                  ▼
           FastAPI Backend
                  │
        ┌─────────┼──────────┐
        ▼         ▼          ▼
    CrewAI    Google Gemini  Pinecone
                  │
                  ▼
              SQLite Database
```

---

# Local Development

## Backend

Start the FastAPI server:

```bash
uv run uvicorn app.api.main:app --reload
```

Backend URL:

```text
http://127.0.0.1:8000
```

Swagger Documentation:

```text
http://127.0.0.1:8000/docs
```

---

## Frontend

Open another terminal.

Run:

```bash
uv run streamlit run frontend/app.py
```

Frontend URL:

```text
http://localhost:8501
```

---

# Required Environment Variables

Create a `.env` file using `.env.example`.

Example:

```env
GOOGLE_API_KEY=your_google_api_key

PINECONE_API_KEY=your_pinecone_api_key

PINECONE_INDEX=support-kb
```

Never expose production API keys in your repository.

---

# Production Deployment

The project has been designed so that the frontend and backend can be deployed independently.

Recommended architecture:

```text
Streamlit Cloud
        │
        ▼
FastAPI (Render / Railway / Fly.io)
        │
        ▼
Google Gemini
        │
        ▼
Pinecone
        │
        ▼
PostgreSQL (Recommended)
```

---

# Recommended Hosting Platforms

## FastAPI Backend

Recommended providers:

* Render
* Railway
* Fly.io
* Azure App Service
* Google Cloud Run
* AWS ECS

---

## Streamlit Frontend

Recommended providers:

* Streamlit Community Cloud
* Render
* Railway

---

## Database

Current implementation:

* SQLite

Recommended for production:

* PostgreSQL
* MySQL

SQLite is suitable for development but not recommended for high-concurrency production environments.

---

# Pinecone

SupportFlow AI uses Pinecone as the vector database for Retrieval-Augmented Generation (RAG).

Before deployment:

* Create a Pinecone project
* Create an index
* Upload knowledge base documents
* Configure API credentials

---

# Google Gemini

SupportFlow AI currently uses Google Gemini for all language model tasks.

Before deployment:

* Generate an API key from Google AI Studio
* Store the key securely as an environment variable
* Do not hardcode credentials

The modular architecture allows Gemini to be replaced with providers such as:

* OpenAI GPT
* Anthropic Claude
* Groq
* Ollama
* Azure OpenAI

with minimal code changes.

---

# Deployment Checklist

Before deploying, verify:

* Python 3.12 installed
* Environment variables configured
* Pinecone index created
* Knowledge base ingested
* Dependencies installed
* FastAPI starts successfully
* Streamlit connects to the backend
* API endpoints respond correctly

---

# Docker (Future Enhancement)

Docker support is planned for future releases.

A production deployment may include:

```text
Docker Compose

├── FastAPI
├── Streamlit
├── PostgreSQL
└── Redis
```

This would simplify local development and cloud deployment.

---

# CI/CD (Future Enhancement)

Potential CI/CD pipeline:

```text
GitHub Push
      │
      ▼
GitHub Actions
      │
      ▼
Run Tests
      │
      ▼
Build Application
      │
      ▼
Deploy Backend
      │
      ▼
Deploy Frontend
```

This enables automated testing and deployments.

---

# Monitoring (Future Enhancement)

Recommended production monitoring stack:

* Prometheus
* Grafana
* Sentry
* UptimeRobot

These tools help monitor:

* API availability
* Response times
* Error rates
* System health

---

# Security Considerations

For production deployments:

* Store secrets in environment variables
* Enable HTTPS
* Add JWT authentication
* Configure CORS
* Implement rate limiting
* Restrict API access where appropriate

---

# Deployment Status

Current Status:

| Component           | Status              |
| ------------------- | ------------------- |
| FastAPI Backend     | ✅ Local Development |
| Streamlit Dashboard | ✅ Local Development |
| Google Gemini       | ✅ Integrated        |
| Pinecone            | ✅ Integrated        |
| SQLite              | ✅ Integrated        |
| Cloud Deployment    | ⏳ Planned           |

---

# Future Roadmap

Planned deployment improvements include:

* Docker support
* PostgreSQL migration
* Authentication (JWT)
* CI/CD with GitHub Actions
* Kubernetes deployment
* Redis caching
* Monitoring and logging
* Live production demo

---

# Summary

SupportFlow AI has been architected with a modular design that supports future cloud deployment and scalability.

While the current implementation is optimized for local development and demonstration, the application can be extended for production use by replacing SQLite with PostgreSQL, deploying the backend and frontend independently, and introducing authentication, monitoring, and CI/CD automation.
