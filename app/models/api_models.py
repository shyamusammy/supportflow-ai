from pydantic import BaseModel


class SupportRequest(BaseModel):
    message: str


class SupportResponse(BaseModel):

    ticket_id: str

    category: str
    priority: str
    sentiment: str

    customer_response: str

    escalate: bool
    reason: str
    assigned_team: str