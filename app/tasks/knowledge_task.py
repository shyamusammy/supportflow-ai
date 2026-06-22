from crewai import Task

from app.models.knowledge import KnowledgeOutput
from app.agents.knowledge_agent import knowledge_agent


def create_knowledge_task(intent_task, customer_message):

    return Task(
        description=f"""
        Use the Knowledge Base Retriever tool.

        Read the classification result from the
        previous task.

        Extract:
        - Category
        - Priority
        - Sentiment

        Use the category as the department
        parameter when calling the tool.

        Examples:

        Billing -> billing
        Login -> login
        Refund -> refund
        Subscription -> subscription
        Security -> security

        IMPORTANT:

        Use the ORIGINAL customer message below
        as the query parameter:

        Customer Message:
        {customer_message}

        Search only the relevant department
        documents and return the best matching
        knowledge.

        Return:
        - Relevant documents
        - Recommended resolution

        Always use the tool before answering.
        """,

        expected_output="""
        Relevant documents and
        recommended solution.
        """,

        context=[intent_task],

        output_pydantic=KnowledgeOutput,

        agent=knowledge_agent
    )