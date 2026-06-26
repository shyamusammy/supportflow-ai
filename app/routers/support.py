from fastapi import APIRouter

from app.crews.support_crew import run_support_crew

from app.models.api_models import (SupportRequest,SupportResponse)

from app.utils.ticket_generator import generate_ticket_id

from app.constants import (GENERAL_SUPPORT,SERVICE_UNAVAILABLE_MESSAGE)

from app.logger import logger

from app.services.ticket_service import save_ticket


router = APIRouter()


@router.post(
    "/support",
    response_model=SupportResponse
)
def process_ticket(request: SupportRequest):

    # Generate ticket ID once
    ticket_id = generate_ticket_id()

    logger.info(
        f"New support request received. "
        f"Ticket ID: {ticket_id}"
    )

    try:

        result = run_support_crew(
            customer_message=request.message
        )

        intent = result["intent"]
        response = result["response"]
        escalation = result["escalation"]

        logger.info(
            f"Ticket {ticket_id} | "
            f"Category={intent.category} | "
            f"Priority={intent.priority} | "
            f"Sentiment={intent.sentiment} | "
            f"Escalated={escalation.escalate}"
        )

        save_ticket(
            ticket_id=ticket_id,
            customer_message=request.message,

            category=intent.category,
            priority=intent.priority,
            sentiment=intent.sentiment,

            customer_response=response.customer_response,

            escalate=escalation.escalate,
            reason=escalation.reason,
            assigned_team=escalation.assigned_team,
            )

        return SupportResponse(
            ticket_id=ticket_id,

            category=intent.category,
            priority=intent.priority,
            sentiment=intent.sentiment,

            customer_response=response.customer_response,

            escalate=escalation.escalate,
            reason=escalation.reason,
            assigned_team=escalation.assigned_team,
        )

    except Exception as e:

        logger.error(
            f"Ticket {ticket_id} failed: {str(e)}"
        )

        return SupportResponse(
            ticket_id=ticket_id,

            category="Unknown",
            priority="Unknown",
            sentiment="Unknown",

            customer_response=SERVICE_UNAVAILABLE_MESSAGE,

            escalate=False,
            reason=str(e),
            assigned_team=GENERAL_SUPPORT,
        )