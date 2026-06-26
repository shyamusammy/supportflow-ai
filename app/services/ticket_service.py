
from app.repositories.ticket_repository import (
    save_ticket_to_db,
    get_all_tickets,
    get_ticket_by_id,
    get_tickets_by_category,
    get_tickets_by_priority,
    get_escalated_tickets,
    get_ticket_analytics,
    search_tickets,
    get_paginated_tickets,

)


def search_for_tickets(query: str):

    return search_tickets(query)


def save_ticket(
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

    return save_ticket_to_db(
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


def fetch_all_tickets():

    return get_all_tickets()


def fetch_ticket(ticket_id: str):

    return get_ticket_by_id(ticket_id)


def fetch_tickets_by_category(category: str):

    return get_tickets_by_category(category)


def fetch_tickets_by_priority(priority: str):

    return get_tickets_by_priority(priority)


def fetch_escalated_tickets():

    return get_escalated_tickets()


def fetch_ticket_analytics():

    return get_ticket_analytics()


def fetch_paginated_tickets(
    page: int = 1,
    limit: int = 20
):

    return get_paginated_tickets(
        page=page,
        limit=limit
    )