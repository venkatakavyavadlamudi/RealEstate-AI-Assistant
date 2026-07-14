from pathlib import Path
from langchain_community.document_loaders import TextLoader


def load_markdown_documents(markdown_directory: Path):
    """
    Loads all Markdown documents recursively from the given directory.

    Args:
        markdown_directory (Path): Path to the Markdown folder.

    Returns:
        list: List of LangChain Document objects.
    """

    documents = []

    markdown_files = markdown_directory.rglob("*.md")

    for markdown_file in markdown_files:
        try:
            loader = TextLoader(str(markdown_file), encoding="utf-8")
            docs = loader.load()

            for doc in docs:
                doc.metadata["source"] = markdown_file.name
                doc.metadata["file_type"] = "markdown"
                doc.metadata["file_path"] = str(markdown_file)

            documents.extend(docs)

        except Exception as e:
            print(f"Error loading {markdown_file.name}: {e}")

    return documents