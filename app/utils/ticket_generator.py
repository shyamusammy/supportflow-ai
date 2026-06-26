from datetime import datetime
import uuid


def generate_ticket_id():

    date = datetime.now().strftime("%Y%m%d")

    unique = str(uuid.uuid4())[:6].upper()

    return f"TICKET-{date}-{unique}"