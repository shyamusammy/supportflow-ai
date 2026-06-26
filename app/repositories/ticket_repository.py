from app.database.database import SessionLocal
from app.database.models import Ticket
from sqlalchemy import desc, or_


def save_ticket_to_db(
    ticket_id: str,
    customer_message: str,
    category: str,
    priority: str,
    sentiment: str,
    customer_response: str,
    escalate: bool,
    reason: str,
    assigned_team: str
):

    db = SessionLocal()

    try:

        ticket = Ticket(
            ticket_id=ticket_id,
            customer_message=customer_message,

            category=category,
            priority=priority,
            sentiment=sentiment,

            customer_response=customer_response,

            escalate=escalate,
            reason=reason,
            assigned_team=assigned_team,
        )

        db.add(ticket)
        db.commit()

    finally:
        db.close()


def get_all_tickets():

    db = SessionLocal()

    try:

        return (
            db.query(Ticket)
            .order_by(desc(Ticket.created_at))
            .all()
        )

    finally:
        db.close()


def get_ticket_by_id(ticket_id: str):

    db = SessionLocal()

    try:

        return (
            db.query(Ticket)
            .filter(Ticket.ticket_id == ticket_id)
            .first()
        )

    finally:
        db.close()


def get_tickets_by_category(category: str):

    db = SessionLocal()

    try:

        return (
            db.query(Ticket)
            .filter(Ticket.category == category)
            .all()
        )

    finally:
        db.close()


def get_tickets_by_priority(priority: str):

    db = SessionLocal()

    try:

        return (
            db.query(Ticket)
            .filter(Ticket.priority == priority)
            .all()
        )

    finally:
        db.close()


def get_escalated_tickets():

    db = SessionLocal()

    try:

        return (
            db.query(Ticket)
            .filter(Ticket.escalate.is_(True))
            .all()
        )

    finally:
        db.close()


def get_ticket_analytics():

    db = SessionLocal()

    try:

        total_tickets = db.query(Ticket).count()

        escalated_tickets = (
            db.query(Ticket)
            .filter(Ticket.escalate.is_(True))
            .count()
        )

        billing_tickets = (
            db.query(Ticket)
            .filter(Ticket.category == "Billing")
            .count()
        )

        login_tickets = (
            db.query(Ticket)
            .filter(Ticket.category == "Login")
            .count()
        )

        refund_tickets = (
            db.query(Ticket)
            .filter(Ticket.category == "Refund")
            .count()
        )

        technical_tickets = (
            db.query(Ticket)
            .filter(Ticket.category == "Technical")
            .count()
        )

        return {
            "total_tickets": total_tickets,
            "escalated_tickets": escalated_tickets,
            "billing_tickets": billing_tickets,
            "login_tickets": login_tickets,
            "refund_tickets": refund_tickets,
            "technical_tickets": technical_tickets
        }

    finally:
        db.close()


def search_tickets(query: str):

    db = SessionLocal()

    try:

        return (
            db.query(Ticket)
            .filter(
                or_(
                    Ticket.customer_message.ilike(f"%{query}%"),
                    Ticket.category.ilike(f"%{query}%"),
                    Ticket.priority.ilike(f"%{query}%"),
                    Ticket.reason.ilike(f"%{query}%"),
                    Ticket.assigned_team.ilike(f"%{query}%")
                )
            )
            .order_by(desc(Ticket.created_at))
            .all()
        )

    finally:
        db.close()


def get_paginated_tickets(
    page: int = 1,
    limit: int = 20
):

    db = SessionLocal()

    try:

        offset = (page - 1) * limit

        return (
            db.query(Ticket)
            .order_by(desc(Ticket.created_at))
            .offset(offset)
            .limit(limit)
            .all()
        )

    finally:
        db.close()