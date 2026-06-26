
from fastapi import APIRouter

from app.services.ticket_service import (
    fetch_all_tickets,
    fetch_ticket,
    fetch_tickets_by_category,
    fetch_tickets_by_priority,
    fetch_escalated_tickets,
    fetch_ticket_analytics,
    search_for_tickets,
    fetch_paginated_tickets

)

router = APIRouter()


# Get all tickets
@router.get("/tickets")
def get_tickets(
    page: int = 1,
    limit: int = 20
):

    return fetch_paginated_tickets(
        page=page,
        limit=limit
    )


# Get ticket by ticket ID
@router.get("/tickets/{ticket_id}")
def get_ticket(ticket_id: str):

    ticket = fetch_ticket(ticket_id)

    if not ticket:
        return {
            "message": "Ticket not found"
        }

    return ticket


# Get tickets by category
@router.get("/tickets/category/{category}")
def tickets_by_category(category: str):

    return fetch_tickets_by_category(category)


# Get tickets by priority
@router.get("/tickets/priority/{priority}")
def tickets_by_priority(priority: str):

    return fetch_tickets_by_priority(priority)


# Get escalated tickets
@router.get("/tickets/escalated")
def escalated_tickets():

    return fetch_escalated_tickets()


# Analytics
@router.get("/analytics")
def analytics():

    return fetch_ticket_analytics()


#ticket_search
@router.get("/tickets/search/{query}")
def search(query: str):

    return search_for_tickets(query)