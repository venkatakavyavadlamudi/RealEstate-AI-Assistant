from loaders.document_loader import load_documents
from rag.chunker import split_documents

documents = load_documents()

chunks = split_documents(documents)

print("\nFirst Chunk Metadata:")
print(chunks[0].metadata)

print("\nFirst Chunk:\n")
print(chunks[0].page_content[:500])