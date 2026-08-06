import re

from services.llm import get_llm
from services.tool import calculator
from services.chatbot import ask_question

llm = get_llm()


def run_agent(question: str, vectordb=None):

    question = question.strip()

    # Calculator Tool
    if re.fullmatch(r"[0-9+\-*/(). ]+", question):
        return calculator(question),[]
    
    if vectordb is not None:
        # Search in Vector DB
        docs = vectordb.similarity_search_with_score(
            question,
            k=1
        )

        # If relevant document found → use RAG
        if docs:
            doc, score = docs[0]

            # Lower score = Better match
            if score < 0.8:
                answer, docs= ask_question(vectordb, question)
                return answer[0]["text"],docs

    # Otherwise use Gemini
    response = llm.invoke(question)
    return response.content[0]["text"],[]