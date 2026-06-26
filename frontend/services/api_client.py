import requests

BASE_URL = "http://127.0.0.1:8000"


def get_tickets():

    response = requests.get(
        f"{BASE_URL}/tickets?limit=5"
    )

    return response.json()


def get_analytics():

    response = requests.get(
        f"{BASE_URL}/analytics"
    )

    return response.json()


def search_tickets(query: str):

    response = requests.get(
        f"{BASE_URL}/tickets/search/{query}"
    )

    return response.json()