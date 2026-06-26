# 🌐 SupportFlow AI — API Documentation

This document describes the REST API provided by **SupportFlow AI**.

The API is built with **FastAPI** and serves as the communication layer between the Streamlit frontend and the AI-powered backend.

---

# 📍 Base URL

Local Development

```text
http://127.0.0.1:8000
```

Interactive Swagger Documentation

```text
http://127.0.0.1:8000/docs
```

---

# API Overview

SupportFlow AI exposes endpoints for:

* Processing customer support requests
* Retrieving ticket history
* Searching tickets
* Viewing analytics

---

# POST /support

Processes a customer support request using the CrewAI multi-agent workflow.

### Request

```http
POST /support
```

### Request Body

```json
{
    "message": "I was charged twice for my subscription."
}
```

### Successful Response

```json
{
    "ticket_id": "TICKET-20260624-111A76",
    "category": "Billing",
    "priority": "High",
    "sentiment": "Negative",
    "customer_response": "Thank you for reaching out...",

    "escalate": false,
    "reason": "Duplicate charge covered by billing policy.",
    "assigned_team": "Billing Department"
}
```

### Processing Pipeline

The endpoint performs:

1. Request validation
2. Intent classification
3. Knowledge retrieval (RAG)
4. Google Gemini response generation
5. Escalation decision
6. Ticket storage
7. JSON response

---

# GET /tickets

Returns all processed tickets.

### Request

```http
GET /tickets
```

### Query Parameters

| Parameter | Type    | Default | Description      |
| --------- | ------- | ------- | ---------------- |
| page      | Integer | 1       | Page number      |
| limit     | Integer | 20      | Tickets per page |

### Response

```json
[
    {
        "ticket_id":"...",
        "category":"Billing",
        "priority":"High",
        "assigned_team":"Billing Department"
    }
]
```

---

# GET /tickets/{ticket_id}

Returns a single ticket.

### Example

```http
GET /tickets/TICKET-20260624-111A76
```

### Response

```json
{
    "ticket_id":"...",
    "customer_message":"...",
    "category":"Billing",
    "priority":"High",
    "sentiment":"Negative",
    "customer_response":"...",
    "escalate":false,
    "assigned_team":"Billing Department"
}
```

---

# GET /tickets/category/{category}

Returns tickets filtered by category.

Example:

```http
GET /tickets/category/Billing
```

Supported categories include:

* Billing
* Login
* Refund
* Technical

---

# GET /tickets/priority/{priority}

Returns tickets filtered by priority.

Example

```http
GET /tickets/priority/High
```

Supported priorities include:

* Low
* Medium
* High
* Critical

---

# GET /tickets/escalated

Returns only escalated tickets.

Example

```http
GET /tickets/escalated
```

Response

```json
[
    {
        "ticket_id":"...",
        "assigned_team":"Security Operations Center"
    }
]
```

---

# GET /analytics

Returns dashboard analytics.

### Request

```http
GET /analytics
```

### Response

```json
{
    "total_tickets":25,
    "escalated_tickets":4,
    "billing_tickets":8,
    "login_tickets":6,
    "refund_tickets":5,
    "technical_tickets":6
}
```

The Streamlit dashboard consumes this endpoint to generate charts and KPI cards.

---

# Error Responses

Typical API responses include:

## 200 OK

Request completed successfully.

## 404 Not Found

Requested ticket could not be found.

Example:

```json
{
    "message":"Ticket not found"
}
```

## 422 Validation Error

Returned when the request body is invalid.

Example:

```json
{
    "detail":[
        {
            "msg":"Field required"
        }
    ]
}
```

## 500 Internal Server Error

Returned when an unexpected server-side error occurs.

---

# Authentication

The current implementation does **not** require authentication.

For production deployments, recommended improvements include:

* JWT Authentication
* OAuth 2.0
* API Keys
* Role-Based Access Control (RBAC)

---

# API Architecture

```text
Streamlit Dashboard
        │
        ▼
FastAPI REST API
        │
        ▼
CrewAI
        │
        ▼
Gemini + Pinecone
        │
        ▼
SQLite
```

---

# Future API Enhancements

Potential future endpoints include:

```http
POST /feedback

POST /upload-knowledge

DELETE /tickets/{ticket_id}

PUT /tickets/{ticket_id}

GET /health

GET /metrics
```

These additions would further support production deployments and system monitoring.

---

# Summary

The SupportFlow AI REST API provides a clean interface for interacting with the multi-agent customer support platform.

By separating the frontend from the AI workflow, the API enables future integrations with web applications, mobile clients, chatbots, and third-party services.
