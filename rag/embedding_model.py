from langchain_google_genai import GoogleGenerativeAIEmbeddings
from utils.config import GOOGLE_API_KEY, EMBEDDING_MODEL


def get_embedding_model():

    print("API KEY EXISTS:", GOOGLE_API_KEY is not None)
    print("MODEL:", EMBEDDING_MODEL)

    return GoogleGenerativeAIEmbeddings(
        model=EMBEDDING_MODEL,
        google_api_key=GOOGLE_API_KEY
    )
