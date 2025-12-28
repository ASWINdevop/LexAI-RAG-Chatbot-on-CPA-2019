# src/vectordb/store.py
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
import os

DB_PATH = "data/processed/faiss_index"

def create_vector_db(chunks):
    """
    Converts chunks to vectors and saves them to FAISS index.
    """
    # Use a free, high-quality model optimized for CPU
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    
    # Create the vector store
    vector_store = FAISS.from_texts(chunks, embedding=embeddings)
    
    # Save locally
    vector_store.save_local(DB_PATH)
    print(f"Vector database saved to {DB_PATH}")
    return vector_store

def load_vector_db():
    """
    Loads the existing FAISS index.
    """
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    
    if not os.path.exists(DB_PATH):
        raise FileNotFoundError("Vector DB not found. Please run the ingestion pipeline first.")
        
    vector_store = FAISS.load_local(DB_PATH, embeddings, allow_dangerous_deserialization=True)
    return vector_store