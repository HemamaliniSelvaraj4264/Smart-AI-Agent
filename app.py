import streamlit as st

from services.pdf_reader import read_pdf
from services.splitter import split_documents
from services.vectordb import create_vectordb
from services.agent import run_agent

st.set_page_config(
    page_title="Smart AI Agent",
    layout="wide"
)

st.title("🤖 Smart AI Agent")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])    

# ---------------- PDF Upload ----------------
st.sidebar.title("Documents")

if st.sidebar.button("Clear Chat"):
    st.session_state.messages = []
    st.rerun()

upload_files = st.sidebar.file_uploader(
    "Upload PDF",
    type="pdf",
    accept_multiple_files=True
)

vectordb = None

if upload_files:

    with st.spinner("Uploading PDF..."):

        all_documents = []

        for file in upload_files:
            docs = read_pdf(file)
            all_documents.extend(docs)

        chunks = split_documents(all_documents)

        vectordb = create_vectordb(chunks)

        st.sidebar.success(f"{len(upload_files)} PDF(s) Uploaded Successfully!")

    st.sidebar.subheader("Uploaded Files")

    for file in upload_files:
        st.sidebar.write(f"{file.name}")

# ---------------- Chat ----------------

question = st.chat_input("Ask Anything")

if question:

   st.session_state.messages.append(
       {
           "role":"user",
           'content':question
       }
   )

   with st.chat_message("user"):
       st.markdown(question)


   with st.spinner("Thinking..."):
        answer,docs = run_agent(question,vectordb)    

   st.session_state.messages.append(
       {
           "role":"assistant",
           "content":answer
       }
   )

   with st.chat_message("assistant"):
       st.markdown(answer)

   # Display Source page    
   if docs:
       st.markdown("Source")

       shown = set()

       for doc in docs:
           file = doc.metadata.get("source_file","Unknown")
           page = doc.metadata.get("page",0)+ 1

           key = (file,page)

           if key not in shown:
               shown.add(key)
               st.write(f"{file}-Page {page}")