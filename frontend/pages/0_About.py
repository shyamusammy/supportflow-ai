import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="SupportFlow AI",
    page_icon="🤖",
    layout="wide",
)

ASSETS = Path(__file__).parent.parent / "assets"

banner = ASSETS / "supportflow-banner.png"
workflow = ASSETS / "workflow-diagram.png"
architecture = ASSETS / "architecture-diagram.png"

# =====================================================
# Hero Banner
# =====================================================

if banner.exists():
    st.image(str(banner), use_container_width=True)
else:
    st.title("🤖 SupportFlow AI")
    st.subheader(
        "Intelligent Multi-Agent Customer Support Platform"
    )
    st.caption(
        "CrewAI • Gemini • Pinecone RAG • FastAPI • Streamlit"
    )

st.divider()

# =====================================================
# About
# =====================================================

st.header("📖 About SupportFlow AI")

st.write(
    """
SupportFlow AI is a production-inspired customer support platform
that combines **CrewAI**, **Gemini**, and **Pinecone RAG** to
automate customer support operations.

The platform classifies customer intent, retrieves knowledge,
generates intelligent responses, determines escalation, stores
ticket history, and provides analytics through an interactive
dashboard.
"""
)

st.divider()

# =====================================================
# Core Features
# =====================================================

st.header("✨ Core Features")

c1, c2, c3 = st.columns(3)

with c1:

    st.success("🤖 Multi-Agent Workflow")

    st.success("🧠 Intent Classification")

    st.success("📚 Pinecone RAG")

with c2:

    st.success("💬 Gemini AI Responses")

    st.success("🚨 Escalation Engine")

    st.success("🎫 Ticket Management")

with c3:

    st.success("📊 Analytics Dashboard")

    st.success("🔎 Ticket Search")

    st.success("⚡ FastAPI Backend")

st.divider()

# =====================================================
# Tech Stack
# =====================================================

st.header("🛠 Technology Stack")

backend, ai, database, frontend = st.columns(4)

with backend:

    st.markdown("### Backend")

    st.write("• FastAPI")

    st.write("• SQLAlchemy")

    st.write("• Uvicorn")

with ai:

    st.markdown("### AI")

    st.write("• CrewAI")

    st.write("• Gemini")

    st.write("• Prompt Engineering")

with database:

    st.markdown("### Database")

    st.write("• SQLite")

    st.write("• Pinecone")

with frontend:

    st.markdown("### Frontend")

    st.write("• Streamlit")

    st.write("• Plotly")

    st.write("• Pandas")

st.divider()

# =====================================================
# Workflow Diagram
# =====================================================

st.header("🧠 AI Workflow")

if workflow.exists():

    st.image(
        str(workflow),
        use_container_width=True
    )

else:

    st.info(
        "Workflow diagram will appear here."
    )

st.divider()

# =====================================================
# Architecture Diagram
# =====================================================

st.header("🏗️ System Architecture")

if architecture.exists():

    st.image(
        str(architecture),
        use_container_width=True
    )

else:

    st.info(
        "Architecture diagram will appear here."
    )

st.divider()

# =====================================================
# Quick Navigation
# =====================================================

st.header("🚀 Explore SupportFlow AI")

st.write(
    "Navigate through the application using the shortcuts below."
)

nav1, nav2, nav3 = st.columns(3)

with nav1:

    if st.button(
        "📊 Dashboard",
        use_container_width=True,
    ):
        st.switch_page("pages/1_Dashboard.py")

with nav2:

    if st.button(
        "🎫 Ticket History",
        use_container_width=True,
    ):
        st.switch_page("pages/2_Ticket_History.py")

with nav3:

    if st.button(
        "📊 Analytics",
        use_container_width=True,
    ):
        st.switch_page("pages/3_Analytics.py")

st.divider()

# =====================================================
# Footer
# =====================================================

st.caption("SupportFlow AI • Version 1.0")

st.caption(
    "Developed by Shyam Sabbi"
)