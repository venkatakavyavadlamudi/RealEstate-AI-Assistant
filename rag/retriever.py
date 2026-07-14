from rag.vector_store import load_vector_store
from utils.config import FAISS_INDEX_PATH, TOP_K_RESULTS


class Retriever:

    def __init__(self):
        self.vector_store = load_vector_store(FAISS_INDEX_PATH)

    def retrieve(self, query):
        """
        Retrieve the most relevant documents for the user query.
        """

        retriever = self.vector_store.as_retriever(
            search_kwargs={"k": TOP_K_RESULTS}
        )

        documents = retriever.invoke(query)

        return documents