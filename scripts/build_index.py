import sys
from pathlib import Path

# Add project root to Python path
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(PROJECT_ROOT))
from loaders.document_loader import load_documents
from rag.chunker import split_documents
from rag.vector_store import create_vector_store, save_vector_store
from utils.config import FAISS_INDEX_PATH


def main():

    print("=" * 60)
    print("Loading Documents...")
    print("=" * 60)

    documents = load_documents()

    print("=" * 60)
    print("Splitting Documents...")
    print("=" * 60)

    chunks = split_documents(documents)

    print("=" * 60)
    print("Creating FAISS Index...")
    print("=" * 60)

    vector_store = create_vector_store(chunks)

    print("=" * 60)
    print("Saving FAISS Index...")
    print("=" * 60)

    save_vector_store(vector_store, FAISS_INDEX_PATH)

    print("\n✅ Vector Database Created Successfully!")


if __name__ == "__main__":
    main()