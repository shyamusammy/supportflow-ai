import streamlit as st
import pandas as pd

from services.api_client import (
    get_tickets,
    search_tickets,
    get_analytics,
)

# --------------------------------------------------
# Page Config
# --------------------------------------------------

st.set_page_config(
    page_title="Ticket History",
    page_icon="🎫",
    layout="wide",
)

st.title("🎫 Ticket History")

# --------------------------------------------------
# Analytics Summary
# --------------------------------------------------

analytics = get_analytics()

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "📨 Total Tickets",
        analytics.get("total_tickets", 0)
    )

with col2:
    st.metric(
        "🚨 Escalated",
        analytics.get("escalated_tickets", 0)
    )

with col3:
    st.metric(
        "💳 Billing",
        analytics.get("billing_tickets", 0)
    )

with col4:
    st.metric(
        "🔑 Login",
        analytics.get("login_tickets", 0)
    )

st.divider()

# --------------------------------------------------
# Search + Refresh
# --------------------------------------------------

left, right = st.columns([6, 1])

with left:

    query = st.text_input(
        "🔍 Search Tickets",
        placeholder="Search by customer message, category, priority or assigned team..."
    )

with right:

    st.write("")
    st.write("")

    refresh = st.button(
        "🔄 Refresh",
        use_container_width=True
    )

if refresh:
    st.rerun()

st.divider()

# --------------------------------------------------
# Load Data
# --------------------------------------------------

if query.strip():

    tickets = search_tickets(query)

else:

    tickets = get_tickets()

df = pd.DataFrame(tickets)

# --------------------------------------------------
# Display Table
# --------------------------------------------------

if not df.empty:

    columns_to_show = [
        "ticket_id",
        "category",
        "priority",
        "sentiment",
        "assigned_team",
        "escalate",
        "customer_message",
    ]

    df = df[columns_to_show]

    df.rename(
        columns={
            "ticket_id": "Ticket ID",
            "category": "Category",
            "priority": "Priority",
            "sentiment": "Sentiment",
            "assigned_team": "Assigned Team",
            "escalate": "Escalated",
            "customer_message": "Customer Message",
        },
        inplace=True,
    )

    st.caption(f"Showing **{len(df)}** ticket(s)")

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True,
        height=650,
        column_config={
            "Ticket ID": st.column_config.TextColumn(
                width="medium"
            ),
            "Category": st.column_config.TextColumn(
                width="small"
            ),
            "Priority": st.column_config.TextColumn(
                width="small"
            ),
            "Sentiment": st.column_config.TextColumn(
                width="small"
            ),
            "Assigned Team": st.column_config.TextColumn(
                width="medium"
            ),
            "Escalated": st.column_config.CheckboxColumn(
                width="small"
            ),
            "Customer Message": st.column_config.TextColumn(
                width="large"
            ),
        },
    )

else:

    st.info("No matching tickets found.")