from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    DateTime
)

from datetime import datetime

from app.database.database import Base


class Ticket(Base):

    __tablename__ = "tickets"

    id = Column(Integer, primary_key=True, index=True)

    ticket_id = Column(String, unique=True)

    customer_message = Column(String)

    category = Column(String)
    priority = Column(String)
    sentiment = Column(String)

    customer_response = Column(String)

    escalate = Column(Boolean)

    reason = Column(String)

    assigned_team = Column(String)

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )