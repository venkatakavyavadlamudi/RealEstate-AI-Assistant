from langchain_community.vectorstores import FAISS

from rag.embedding_model import get_embedding_model


def create_vector_store(chunks):
    """
    Creates a FAISS vector store from document chunks.
    """

    embeddings = get_embedding_model()

    batch_size = 50
    vector_store = None

    for i in range(0, len(chunks), batch_size):
        batch = chunks[i:i + batch_size]

        print(f"Embedding batch {i//batch_size + 1}")

        if vector_store is None:
            vector_store = FAISS.from_documents(
                documents=batch,
                embedding=embeddings
            )
        else:
            vector_store.add_documents(batch)

        import time
        time.sleep(35)

    return vector_store

def save_vector_store(vector_store, save_path):
    """
    Saves the FAISS index locally.
    """

    vector_store.save_local(str(save_path))


def load_vector_store(save_path):
    """
    Loads an existing FAISS index.
    """

    embeddings = get_embedding_model()

    return FAISS.load_local(
        str(save_path),
        embeddings,
        allow_dangerous_deserialization=True
    )