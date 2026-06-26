from fastapi import FastAPI

from app.routers.support import router as support_router

from app.database.init_db import init_db

from app.routers.ticket import router as ticket_router

init_db()

app = FastAPI(
    title="SupportFlow AI",
    description="Intelligent Multi-Agent Customer Support Platform powered by CrewAI, Gemini, Pinecone RAG, FastAPI and Streamlit.",
    version="1.0.0",
)


# Root endpoint
@app.get("/")
def root():
    return {
        "status": "healthy",
        "service": "AI Customer Support Agent"
    }


# Health check endpoint
@app.get("/health")
def health():
    return {
        "status": "ok"
    }


# Support endpoint
app.include_router(support_router)

app.include_router(ticket_router)