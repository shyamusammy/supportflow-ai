from pydantic import BaseModel

class IntentOutput(BaseModel):
    category: str
    priority: str
    sentiment: str