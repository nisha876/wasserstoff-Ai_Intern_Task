📄 Gen-AI Document Chatbot
A document research and theme synthesis chatbot powered by semantic search and language models. This app allows users to upload multiple documents, ask natural language questions, and get summarized answers with citations and theme extraction.

🔧 Features
✅ Upload scanned or text-based documents (PDF, TXT, PNG, JPG, JPEG)
✅ OCR support for image-based PDFs using Tesseract
✅ Extracts and chunks text, stores in vector database (ChromaDB)
✅ Semantic search using sentence-transformers
✅ Query processing with FastAPI backend
✅ Clickable citations and document filters in Streamlit UI
✅ Theme synthesis and summary generation
✅ Docker-based deployment on Hugging Face Spaces
✅ FastAPI backend hosted on Render

🚀 Demo
Frontend (Streamlit): https://huggingface.co/spaces//
Backend (FastAPI): https://your-fastapi-app.onrender.com

🗂 Project Structure
├── app.py # Streamlit frontend ├── main.py # FastAPI entry point ├── routes.py # Upload/query endpoints ├── extractor.py # PDF/OCR text extraction ├── vector_store.py # Chroma vector database logic ├── embedding.py # Sentence transformer for embeddings ├── llm.py # Theme synthesis (LLM response) ├── Dockerfile # Docker config for Hugging Face ├── requirements.txt # Python dependencies └── README.md

📦 Deployment
Frontend (Streamlit) on Hugging Face
SDK: Docker
Upload app.py, Dockerfile, requirements.txt
Backend (FastAPI) on Render
Start command: uvicorn app.main:app --host 0.0.0.0 --port 10000

Exposed URL used in app.py as BACKEND_URL

🧪 Example Questions to Try
What does SEBI’s new disclosure policy require from listed companies?
What are the key education reforms across the documents?
What environmental themes are identified in recent circulars?
🤖 Models & Tools Used
sentence-transformers (MiniLM) for semantic vector search
Tesseract OCR for scanned PDFs
ChromaDB for in-memory vector storage
Streamlit for UI
FastAPI for backend API
Docker for deployment
✍️ Author
Built with Nisha Kumari
For Wasserstoff Gen-AI Internship Task

