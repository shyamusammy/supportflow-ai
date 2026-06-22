from crewai import Crew, Process

from app.agents.Intent_Classifier_Agent import intent_classifier_Agent
from app.agents.knowledge_agent import knowledge_agent
from app.agents.response_agent import response_agent
from app.agents.escalation_agent import escalation_agent

from app.tasks.intent_task import create_intent_task
from app.tasks.knowledge_task import create_knowledge_task
from app.tasks.response_task import create_response_task
from app.tasks.escalation_task import create_escalation_task


def run_support_crew(customer_message: str):

    # Task 1
    intent_task = create_intent_task(customer_message)

    # Task 2
    knowledge_task = create_knowledge_task(
        intent_task,
        customer_message
    )

    # Task 3
    response_task = create_response_task(
        intent_task,
        knowledge_task,
    )

    # Task 4
    escalation_task = create_escalation_task(
        intent_task,
        knowledge_task,
        response_task,
    )

    crew = Crew(
        agents=[
            intent_classifier_Agent,
            knowledge_agent,
            response_agent,
            escalation_agent,
        ],
        tasks=[
            intent_task,
            knowledge_task,
            response_task,
            escalation_task,
        ],
        process=Process.sequential,
        memory=False,
        verbose=True,
    )

    return crew.kickoff()