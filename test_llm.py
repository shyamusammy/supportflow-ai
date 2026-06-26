# test_llm.py

from app.services.llm import llm

response = llm.call(
    "Reply with exactly: Hello"
)

print(response)