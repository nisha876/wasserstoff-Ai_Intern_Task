from fastapi import APIRouter, UploadFile, File, Form
from app.core.extractor import extract_text
from app.services.vector_store import store_doc_chunks as add_to_vector_store
from app.services.vector_store import search_similar_chunks as query_vector_store
from app.services.llm import generate_theme_summary

router = APIRouter()

@router.post("/upload/")
async def upload_document(file: UploadFile = File(...)):
    text = await extract_text(file)  # ✅ FIXED: added await
    add_to_vector_store(file.filename, text)
    return {"message": f"{file.filename} uploaded and processed."}

@router.post("/ask/")
async def ask_question(question: str = Form(...)):
    answers = query_vector_store(question)
    summary, themes = generate_theme_summary(question, answers)
    return {
        "raw_answers": answers,
        "summary": summary,
        "themes": themes
    }

