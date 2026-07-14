from pathlib import Path
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# ==========================
# Project Paths
# ==========================

# Root project directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Dataset directory
DATA_DIR = BASE_DIR / "data" / "real_estate_kb_dataset"

# Vector database directory
VECTOR_DB_DIR = BASE_DIR / "vector_db"

# ==========================
# Gemini Configuration
# ==========================

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

print("GOOGLE_API_KEY =", GOOGLE_API_KEY)

if GOOGLE_API_KEY is None:
    raise Exception("GOOGLE_API_KEY NOT FOUND")
# ==========================
# Supported File Types
# ==========================

SUPPORTED_EXTENSIONS = [
    ".pdf",
    ".docx",
    ".html",
    ".md"
]

# ==========================
# Text Chunking
# ==========================

CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200

# ==========================
# Retrieval
# ==========================

TOP_K_RESULTS = 5

# ==========================
# Login Credentials
# ==========================

USERNAME = "admin"
PASSWORD = "admin123"

# ==========================
# Embedding Model
# ==========================
EMBEDDING_MODEL = "models/gemini-embedding-001"

# ==========================
# Gemini Model
# ==========================

LLM_MODEL = "gemini-3.1-flash-lite"

# ==========================
# Vector Store
# ==========================

FAISS_INDEX_PATH = VECTOR_DB_DIR / "faiss_index"
