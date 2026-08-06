from services.llm import get_llm

def search_documents(vector_store, question):
    return vector_store.similarity_search(question, k=3)


def ask_question(vector_store, question):

    docs = vector_store.similarity_search(
        question,
        k=3
    )

    context = "\n\n".join(
        doc.page_content for doc in docs
    )

    prompt = f"""
You are a helpful AI assistant.

Answer ONLY from the context below.

If the answer is not available, say:
"I don't know based on the document."

Context:
{context}

Question:
{question}

Answer:
"""

    llm = get_llm()

    response = llm.invoke(prompt)

    return response.content,docs