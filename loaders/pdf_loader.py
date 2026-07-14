from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader


def load_pdf_documents(pdf_directory: Path):
    """
    Loads all PDF documents recursively from the given directory.

    Args:
        pdf_directory (Path): Path to the PDF folder.

    Returns:
        list: List of LangChain Document objects.
    """

    documents = []

    # Search recursively for all PDF files
    pdf_files = pdf_directory.rglob("*.pdf")

    for pdf_file in pdf_files:
        try:
            loader = PyPDFLoader(str(pdf_file))
            docs = loader.load()

            # Add useful metadata
            for doc in docs:
                doc.metadata["source"] = pdf_file.name
                doc.metadata["file_type"] = "pdf"
                doc.metadata["file_path"] = str(pdf_file)

            documents.extend(docs)

        except Exception as e:
            print(f"Error loading {pdf_file.name}: {e}")

    return documents