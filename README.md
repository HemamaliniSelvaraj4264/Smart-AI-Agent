# Smart AI Agent

An AI-powered assistant built using Python, Streamlit, LangChain, Google Gemini, and ChromaDB. The application can answer general questions, solve mathematical expressions, and perform document-based question answering using Retrieval-Augmented Generation (RAG).

## Features

- General AI Chat using Google Gemini
- PDF Upload
- Multiple PDF Support
- Retrieval-Augmented Generation (RAG)
- ChromaDB Vector Database
- Semantic Search
- Calculator Tool
- Automatic Tool Routing
- Chat History
- Source Page Display
- Loading Spinner

## Tech Stack

- Python
- Streamlit
- Google Gemini
- LangChain
- ChromaDB
- HuggingFace Embeddings
- PyPDF

## Project Structure

```text
Smart AI Agent/
│
├── app.py
├── services/
│   ├── agent.py
│   ├── chatbot.py
│   ├── embeddings.py
│   ├── llm.py
│   ├── pdf_reader.py
│   ├── splitter.py
│   ├── tool.py
│   └── vectordb.py
│
├── requirements.txt
├── .env
└── README.md
```

## Installation

```bash
git clone <repository-url>

cd Smart-AI-Agent

pip install -r requirements.txt

streamlit run app.py
```

## How It Works

1. Upload one or more PDF documents.
2. Documents are split into smaller chunks.
3. Embeddings are generated for each chunk.
4. Chunks are stored in ChromaDB.
5. User questions are routed automatically:
   - Mathematical expressions → Calculator
   - Questions about uploaded PDFs → RAG
   - General questions → Google Gemini

## Example Questions

- What is Artificial Intelligence?
- What is Planning?
- Summarize the uploaded document.
- 45 * 25

## Future Improvements

- Voice Input
- Image Understanding
- Web Search Integration
- Multi-Agent Workflow

## License

This project is developed for learning and portfolio purposes.