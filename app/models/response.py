from pydantic import BaseModel

class ResponseOutput(BaseModel):
    customer_response: str