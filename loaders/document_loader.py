from utils.config import DATA_DIR

from loaders.pdf_loader import load_pdf_documents
from loaders.docx_loader import load_docx_documents
from loaders.html_loader import load_html_documents
from loaders.markdown_loader import load_markdown_documents


def load_documents():
    """
    Loads all supported documents from the dataset.

    Returns:
        list: Combined list of LangChain Document objects.
    """

    all_documents = []

    # Load PDFs
    pdf_docs = load_pdf_documents(DATA_DIR / "pdf")
    print(f"Loaded {len(pdf_docs)} PDF pages")
    all_documents.extend(pdf_docs)

    # Load DOCX
    docx_docs = load_docx_documents(DATA_DIR / "docx")
    print(f"Loaded {len(docx_docs)} DOCX documents")
    all_documents.extend(docx_docs)

    # Load HTML
    html_docs = load_html_documents(DATA_DIR / "html")
    print(f"Loaded {len(html_docs)} HTML documents")
    all_documents.extend(html_docs)

    # Load Markdown
    markdown_docs = load_markdown_documents(DATA_DIR / "markdown")
    print(f"Loaded {len(markdown_docs)} Markdown documents")
    all_documents.extend(markdown_docs)

    print(f"\nTotal Documents Loaded: {len(all_documents)}")

    return all_documents