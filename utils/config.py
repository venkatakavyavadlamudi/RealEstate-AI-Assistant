import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

EMBEDDING_MODEL = os.getenv(
    "EMBEDDING_MODEL",
    "models/gemini-embedding-001"
)

LLM_MODEL = os.getenv(
    "LLM_MODEL",
    "gemini-flash-lite-latest"
)

# Data paths
DATA_DIR = BASE_DIR / "data" / "real_estate_kb_dataset"

# FAISS
FAISS_INDEX_PATH = BASE_DIR / "vector_db" / "faiss_index"

# Retrieval
TOP_K_RESULTS = int(
    os.getenv("TOP_K_RESULTS", 5)
)

# Text chunking
CHUNK_SIZE = int(
    os.getenv("CHUNK_SIZE", 1000)
)

CHUNK_OVERLAP = int(
    os.getenv("CHUNK_OVERLAP", 200)
)
