from loaders.document_loader import load_documents

documents = load_documents()

print("\nFirst Document Metadata:")
print(documents[0].metadata)

print("\nFirst 300 Characters:")
print(documents[0].page_content[:300])