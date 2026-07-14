from pathlib import Path
from langchain_community.document_loaders import BSHTMLLoader


def load_html_documents(html_directory: Path):
    """
    Loads all HTML documents recursively from the given directory.

    Args:
        html_directory (Path): Path to the HTML folder.

    Returns:
        list: List of LangChain Document objects.
    """

    documents = []

    html_files = html_directory.rglob("*.html")

    for html_file in html_files:
        try:
            loader = BSHTMLLoader(str(html_file))
            docs = loader.load()

            for doc in docs:
                doc.metadata["source"] = html_file.name
                doc.metadata["file_type"] = "html"
                doc.metadata["file_path"] = str(html_file)

            documents.extend(docs)

        except Exception as e:
            print(f"Error loading {html_file.name}: {e}")

    return documents