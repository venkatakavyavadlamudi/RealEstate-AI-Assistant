from langchain_text_splitters import RecursiveCharacterTextSplitter
from utils.config import CHUNK_SIZE, CHUNK_OVERLAP


def split_documents(documents):
    """
    Split documents into smaller chunks for efficient retrieval.

    Args:
        documents (list): List of LangChain Document objects.

    Returns:
        list: List of chunked Document objects.
    """

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
        separators=["\n\n", "\n", ".", " ", ""]
    )

    chunks = text_splitter.split_documents(documents)

    print(f"\nTotal Chunks Created: {len(chunks)}")

    return chunks