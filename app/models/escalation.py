from pydantic import BaseModel

class EscalationOutput(BaseModel):
    escalate: bool
    reason: str
    assigned_team: str