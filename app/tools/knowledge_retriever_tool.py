import json
from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field

from app.knowledge.retrieval import retrieve_documents


class KnowledgeRetrieverInput(BaseModel):
    query: str = Field(
        ...,
        description="Customer issue or question"
    )

    department: str = Field(
        ...,
        description="Issue category such as billing, login, refund, security, subscription"
    )


class KnowledgeRetrieverTool(BaseTool):
    name: str = "Knowledge Base Retriever"
    description: str = (
        "Searches the company knowledge base "
        "and returns relevant support documents."
    )

    args_schema: Type[BaseModel] = KnowledgeRetrieverInput

    def _run(
            self,
            query: str,
            department: str
            ) -> str:

        documents = retrieve_documents(
            query=query,
            department=department.lower()
        )

        if not documents:
            return "No relevant documents found."

        return json.dumps(
            {
                "documents": documents,
                "count": len(documents)
            },
            indent=2
        )