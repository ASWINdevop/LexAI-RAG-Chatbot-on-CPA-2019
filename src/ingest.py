# src/ingest.py
from data_loader import load_pdf
from preprocess.chunker import chunk_text
from vectordb.store import create_vector_db
import os

# Define paths
PDF_PATH = "data/raw/cpa_2019.pdf"

def main():
    print("1. Loading PDF...")
    raw_text = load_pdf(PDF_PATH)
    
    print(f"2. Chunking text (Total length: {len(raw_text)})...")
    chunks = chunk_text(raw_text)
    print(f"   Created {len(chunks)} chunks.")
    
    print("3. Creating Vector Store (this may take a minute)...")
    create_vector_db(chunks)
    
    print("Done! Knowledge base is ready.")

if __name__ == "__main__":
    main()