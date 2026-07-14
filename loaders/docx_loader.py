from pathlib import Path
from langchain_community.document_loaders import Docx2txtLoader


def load_docx_documents(docx_directory: Path):
    """
    Loads all DOCX documents recursively from the given directory.

    Args:
        docx_directory (Path): Path to the DOCX folder.

    Returns:
        list: List of LangChain Document objects.
    """

    documents = []

    docx_files = docx_directory.rglob("*.docx")

    for docx_file in docx_files:
        try:
            loader = Docx2txtLoader(str(docx_file))
            docs = loader.load()

            for doc in docs:
                doc.metadata["source"] = docx_file.name
                doc.metadata["file_type"] = "docx"
                doc.metadata["file_path"] = str(docx_file)

            documents.extend(docs)

        except Exception as e:
            print(f"Error loading {docx_file.name}: {e}")

    return documents