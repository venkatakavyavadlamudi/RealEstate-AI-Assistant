from loaders.markdown_loader import load_markdown_documents
from utils.config import DATA_DIR

markdown_path = DATA_DIR / "markdown"

documents = load_markdown_documents(markdown_path)

print(f"Total Markdown Documents Loaded: {len(documents)}")

if documents:
    print("\nMetadata:")
    print(documents[0].metadata)

    print("\nFirst 500 Characters:")
    print(documents[0].page_content[:500])