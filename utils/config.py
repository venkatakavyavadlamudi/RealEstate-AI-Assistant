import os

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "models/embedding-001")
print("=" * 50)
print("GOOGLE_API_KEY FOUND:", GOOGLE_API_KEY is not None)
print("KEY LENGTH:", len(GOOGLE_API_KEY) if GOOGLE_API_KEY else 0)
print("=" * 50)
