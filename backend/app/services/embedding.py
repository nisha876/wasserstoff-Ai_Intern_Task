import os
from langchain_community.embeddings import OpenAIEmbeddings

# Ensure the key is picked up
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

def embed(text):
    model = OpenAIEmbeddings()
    return model.embed_query(text)
