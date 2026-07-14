from loaders.html_loader import load_html_documents
from utils.config import DATA_DIR

html_path = DATA_DIR / "html"

documents = load_html_documents(html_path)

print(f"Total HTML Documents Loaded: {len(documents)}")

if documents:
    print("\nMetadata:")
    print(documents[0].metadata)

    print("\nFirst 500 Characters:")
    print(documents[0].page_content[:500])