from pydantic import BaseModel

class KnowledgeOutput(BaseModel):
    relevant_documents: list[str]
    recommended_solution: str
    assigned_team: str | None = None
    policy_priority: str | None = None