from loaders.docx_loader import load_docx_documents
from utils.config import DATA_DIR

docx_path = DATA_DIR / "docx"

documents = load_docx_documents(docx_path)

print(f"Total DOCX Documents Loaded: {len(documents)}")

if documents:
    print("\nMetadata:")
    print(documents[0].metadata)

    print("\nFirst 500 Characters:")
    print(documents[0].page_content[:500])