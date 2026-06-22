from crewai import Task

from app.agents.escalation_agent import escalation_agent
from app.models.escalation import EscalationOutput


def create_escalation_task(
    intent_task,
    knowledge_task,
    response_task,
):
    return Task(
        description="""
        Determine whether this case requires escalation.

        Use ALL available information:

        - Intent classification
        - Retrieved knowledge documents
        - Recommended resolution
        - Customer response

        IMPORTANT:

        Use the retrieved policies when making
        the escalation decision.

        Escalate if:

        - Security issue
        - Account compromise
        - Fraud
        - Critical outage
        - High-value refund
        - Regulatory concern
        - Policy explicitly requires escalation
        - Policy assigns a specialized team

        Do NOT escalate simple requests that
        can be resolved automatically.

        Return:
        - Escalation decision
        - Reason
        - Assigned team
        """,
        expected_output="""
        Return escalation decision,
        reason and assigned team.
        """,
        agent=escalation_agent,
        context=[
            intent_task,
            knowledge_task,
            response_task,
        ],
        output_pydantic=EscalationOutput,
    )