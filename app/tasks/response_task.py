from crewai import Task

from app.agents.response_agent import response_agent
from app.models.response import ResponseOutput


def create_response_task(intent_task, knowledge_task):
    return Task(
        description="""
        Create a professional customer response.

        Requirements:
        - Professional
        - Empathetic
        - Clear
        - Actionable

        Use BOTH:
        - The intent classification
        - The retrieved knowledge

        IMPORTANT:

        If knowledge documents were retrieved:

        - Base the response on the retrieved policies.
        - Mention key actions from the policy.
        - Mention timelines if provided.
        - Mention the responsible team if provided.
        - Do not invent policies.

        If no documents were retrieved:

        - Politely explain that no relevant policy was found.
        - Ask for more information if needed.

        Always ground your response in the retrieved knowledge.
        """,
        expected_output="""
        Return a customer-facing response.
        """,
        agent=response_agent,
        context=[intent_task, knowledge_task],
        output_pydantic=ResponseOutput,
    )