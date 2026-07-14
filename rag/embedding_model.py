from langchain_google_genai import GoogleGenerativeAIEmbeddings
from utils.config import GOOGLE_API_KEY, EMBEDDING_MODEL


def get_embedding_model():
    print("GOOGLE_API_KEY exists:", GOOGLE_API_KEY is not None)

    if GOOGLE_API_KEY:
        print("GOOGLE_API_KEY length:", len(GOOGLE_API_KEY))
    else:
        print("GOOGLE_API_KEY is missing")

    embeddings = GoogleGenerativeAIEmbeddings(
        model=EMBEDDING_MODEL,
        google_api_key=GOOGLE_API_KEY
    )

    return embeddings
