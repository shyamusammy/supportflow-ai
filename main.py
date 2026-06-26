from app.crews.support_crew import run_support_crew


def main():

    customer_message = """
    I forgot my password
    """

    result = run_support_crew(customer_message)

    print("\n")
    print("=" * 60)
    print("INTENT")
    print("=" * 60)
    print(result["intent"])

    print("\n")
    print("=" * 60)
    print("KNOWLEDGE")
    print("=" * 60)
    print(result["knowledge"])

    print("\n")
    print("=" * 60)
    print("RESPONSE")
    print("=" * 60)
    print(result["response"])

    print("\n")
    print("=" * 60)
    print("ESCALATION")
    print("=" * 60)
    print(result["escalation"])


if __name__ == "__main__":
    main()