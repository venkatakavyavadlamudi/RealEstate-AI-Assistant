from pathlib import Path

from loaders.pdf_loader import load_pdf_documents
from utils.config import DATA_DIR

pdf_path = DATA_DIR / "pdf"

documents = load_pdf_documents(pdf_path)

print(f"Total PDF Pages Loaded: {len(documents)}")

if documents:
    print("\nFirst Document Metadata:")
    print(documents[0].metadata)

    print("\nFirst 500 Characters:")
    print(documents[0].page_content[:500])