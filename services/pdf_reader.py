from langchain_community.document_loaders import PyPDFLoader
import tempfile
import os

def read_pdf(upload_file):
    with tempfile.NamedTemporaryFile(delete=False,suffix=".pdf") as temp_file:
        temp_file.write(upload_file.getvalue())
        

        loader = PyPDFLoader(temp_file.name)
        documents = loader.load()
        for doc in documents:
            doc.metadata["source_file"] = upload_file.name

        

        return documents