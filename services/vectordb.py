from langchain_chroma import Chroma
from services.embeddings import get_embeddings



def create_vectordb(chunks):

    

    vectordb = Chroma.from_documents(
        documents=chunks,
        embedding=get_embeddings(),
        persist_directory="chroma_db"
    )

    return vectordb