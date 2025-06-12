import chromadb
from chromadb.config import Settings
from app.services.embedding import embed


client = chromadb.Client(Settings())
collection = client.get_or_create_collection(name="documents")

chunk_size = 300

def store_doc_chunks(doc_name, text):
    chunks = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]
    for i, chunk in enumerate(chunks):
        collection.add(documents=[chunk], ids=[f"{doc_name}_{i}"], metadatas=[{"doc": doc_name, "citation": f"Chunk {i}"}], embeddings=[embed(chunk)])

def search_similar_chunks(question):
    results = collection.query(query_texts=[question], n_results=5, include=["documents", "metadatas"])
    out = []
    for doc, meta in zip(results['documents'][0], results['metadatas'][0]):
        out.append({"text": doc, "doc": meta['doc'], "citation": meta['citation']})
    return out