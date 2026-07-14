from rag.retriever import Retriever

retriever = Retriever()

query = "What is the payment plan for Urban Nest Riverside?"

documents = retriever.retrieve(query)

print("=" * 60)
print(f"Retrieved {len(documents)} Documents")
print("=" * 60)

for i, doc in enumerate(documents, start=1):
    print(f"\nDocument {i}")
    print("-" * 50)
    print("Source :", doc.metadata.get("source"))
    print("Type   :", doc.metadata.get("file_type"))
    print()
    print(doc.page_content[:400])