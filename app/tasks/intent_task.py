from crewai import Task

from app.agents.Intent_Classifier_Agent import intent_classifier_Agent
from app.models.intent import IntentOutput


def create_intent_task(customer_message: str):
    return Task(
        description=f"""
        Analyze the customer's message:

        {customer_message}

        Determine:
        - Issue category
        - Priority level
        - Customer sentiment

        Categories:
        - Login
        - Billing
        - Refund
        - Technical
        - Subscription
        - General

        Priorities:
        - Low
        - Medium
        - High
        - Critical
        """,
        expected_output="""
        Return a structured classification of
        category, priority and sentiment.
        """,
        agent=intent_classifier_Agent,
        output_pydantic=IntentOutput,
    )