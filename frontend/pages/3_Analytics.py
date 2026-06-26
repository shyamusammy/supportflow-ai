import streamlit as st
import plotly.express as px
import pandas as pd

from services.api_client import get_analytics

# --------------------------------------------------
# Page Config
# --------------------------------------------------

st.set_page_config(
    page_title="Analytics",
    page_icon="📊",
    layout="wide",
)

st.title("📊 Analytics Dashboard")
st.caption("Real-time insights into AI customer support performance")

analytics = get_analytics()

# --------------------------------------------------
# KPI Cards
# --------------------------------------------------

total = analytics.get("total_tickets", 0)
escalated = analytics.get("escalated_tickets", 0)

rate = 0

if total > 0:
    rate = round((escalated / total) * 100, 1)

col1, col2, col3 = st.columns(3)

col1.metric(
    "📨 Total Tickets",
    total
)

col2.metric(
    "🚨 Escalated",
    escalated
)

col3.metric(
    "📈 Escalation Rate",
    f"{rate}%"
)

st.divider()

# --------------------------------------------------
# Charts
# --------------------------------------------------

left, right = st.columns(2)

category_data = pd.DataFrame(
    {
        "Category": [
            "Billing",
            "Login",
            "Refund",
            "Technical",
        ],
        "Count": [
            analytics.get("billing_tickets", 0),
            analytics.get("login_tickets", 0),
            analytics.get("refund_tickets", 0),
            analytics.get("technical_tickets", 0),
        ],
    }
)

# Remove empty categories
category_data = category_data[
    category_data["Count"] > 0
]

with left:

    st.subheader("📊 Tickets by Category")

    fig = px.bar(
        category_data,
        x="Category",
        y="Count",
        text="Count",
    )

    fig.update_layout(
        height=320,
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

    st.plotly_chart(
        fig,
        use_container_width=True,
    )

with right:

    st.subheader("🥧 Category Share")

    pie = px.pie(
        category_data,
        names="Category",
        values="Count",
        hole=0.45,
    )

    pie.update_layout(
        height=320,
        margin=dict(
            l=10,
            r=10,
            t=20,
            b=10,
        ),
    )

    st.plotly_chart(
        pie,
        use_container_width=True,
    )

st.divider()

# --------------------------------------------------
# AI Insights
# --------------------------------------------------

st.subheader("💡 AI Insights")

if not category_data.empty:

    top_category = category_data.loc[
        category_data["Count"].idxmax(),
        "Category"
    ]

else:

    top_category = "N/A"

status = "🟢 Healthy"

if rate >= 50:
    status = "🔴 High Escalation"

elif rate >= 30:
    status = "🟡 Monitor"

insight1, insight2 = st.columns(2)

with insight1:

    st.info(
        f"""
**Most Common Category**

{top_category}

**Total Tickets**

{total}
"""
    )

with insight2:

    st.success(
        f"""
**Escalation Rate**

{rate}%

**System Status**

{status}
"""
    )