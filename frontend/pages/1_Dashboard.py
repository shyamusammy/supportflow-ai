import streamlit as st
import pandas as pd
import plotly.express as px

from services.api_client import (
    get_analytics,
    get_tickets,
)

# --------------------------------------------------
# Page Config
# --------------------------------------------------

st.set_page_config(
    page_title="Dashboard",
    page_icon="🏠",
    layout="wide",
)

# --------------------------------------------------
# Load Data
# --------------------------------------------------

analytics = get_analytics()
tickets = get_tickets()

# --------------------------------------------------
# Header
# --------------------------------------------------

st.title("📊 Dashboard")

st.markdown("---")

# --------------------------------------------------
# KPI Cards
# --------------------------------------------------

kpi1, kpi2, kpi3, kpi4 = st.columns(4)

kpi1.metric(
    "📨 Tickets",
    analytics.get("total_tickets", 0)
)

kpi2.metric(
    "🚨 Escalated",
    analytics.get("escalated_tickets", 0)
)

kpi3.metric(
    "💳 Billing",
    analytics.get("billing_tickets", 0)
)

kpi4.metric(
    "🔑 Login",
    analytics.get("login_tickets", 0)
)

st.markdown("---")

# --------------------------------------------------
# Main Dashboard
# --------------------------------------------------

left, right = st.columns([1.6, 1])

# ==================================================
# Recent Tickets
# ==================================================

with left:

    st.subheader("📋 Recent Tickets")

    recent_df = pd.DataFrame(tickets)

    if not recent_df.empty:

        recent_df = recent_df[
            [
                "ticket_id",
                "category",
                "priority",
                "assigned_team",
            ]
        ]

        recent_df = recent_df.rename(
            columns={
                "ticket_id": "Ticket ID",
                "category": "Category",
                "priority": "Priority",
                "assigned_team": "Assigned Team",
            }
        )

        st.dataframe(
            recent_df.head(5),
            use_container_width=True,
            hide_index=True,
            height=220,
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
                "Assigned Team": st.column_config.TextColumn(
                    width="medium"
                ),
            },
        )

    else:

        st.info("No tickets available.")

# ==================================================
# Category Chart
# ==================================================

with right:

    st.subheader("📊 Ticket Categories")

    chart_df = pd.DataFrame(
        {
            "Category": [
                "Billing",
                "Login",
                "Refund",
                "Technical",
            ],
            "Tickets": [
                analytics.get("billing_tickets", 0),
                analytics.get("login_tickets", 0),
                analytics.get("refund_tickets", 0),
                analytics.get("technical_tickets", 0),
            ],
        }
    )

    fig = px.bar(
        chart_df,
        x="Category",
        y="Tickets",
        text="Tickets",
    )

    fig.update_layout(
        height=260,
        margin=dict(
            l=10,
            r=10,
            t=20,
            b=10,
        ),
        xaxis_title=None,
        yaxis_title=None,
        showlegend=False,
    )

    fig.update_traces(
        textposition="outside"
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
    )