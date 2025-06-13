from langchain_community.embeddings import OpenAIEmbeddings
from typing import List

# Create the embedder (uses the env var OPENAI_API_KEY automatically)
embedder = OpenAIEmbeddings()

def embed(text: str) -> List[float]:
    return embedder.embed_query(text)
