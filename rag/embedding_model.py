from langchain_google_genai import GoogleGenerativeAIEmbeddings
from utils.config import GOOGLE_API_KEY, EMBEDDING_MODEL


def get_embedding_model():
    """
    Returns the Google Embedding Model.
    """

    embeddings = GoogleGenerativeAIEmbeddings(
        model=EMBEDDING_MODEL,
        google_api_key=GOOGLE_API_KEY
    )

    return embeddings