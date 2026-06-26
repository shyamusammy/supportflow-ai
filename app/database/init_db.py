from app.database.database import engine, Base
from app.database.models import Ticket


def init_db():
    Base.metadata.create_all(bind=engine)