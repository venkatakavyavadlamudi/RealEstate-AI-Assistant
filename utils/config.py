import os

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
import os

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

EMBEDDING_MODEL = os.getenv(
    "EMBEDDING_MODEL",
    "models/embedding-001"
)

FAISS_INDEX_PATH = os.getenv(
    "FAISS_INDEX_PATH",
    "data/faiss_index"
)

TOP_K_RESULTS = int(
    os.getenv("TOP_K_RESULTS", 5)
)print("=" * 50)
print("GOOGLE_API_KEY FOUND:", GOOGLE_API_KEY is not None)
print("KEY LENGTH:", len(GOOGLE_API_KEY) if GOOGLE_API_KEY else 0)
print("=" * 50)
