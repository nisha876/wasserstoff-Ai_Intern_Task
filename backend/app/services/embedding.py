from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')  # Small and fast

def embed(text: str):
    return model.encode(text).tolist()
