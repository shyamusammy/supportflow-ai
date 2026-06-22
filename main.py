from app.crews.support_crew import run_support_crew

def main():

    customer_message = """
    I forgot my password
    """

    result = run_support_crew(customer_message)

    print("\n")
    print("=" * 60)
    print("FINAL RESULT")
    print("=" * 60)
    print(result)

if __name__ == "__main__":
    main()