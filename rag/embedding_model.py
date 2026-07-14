from langchain_google_genai import GoogleGenerativeAIEmbeddings
from utils.config import GOOGLE_API_KEY, EMBEDDING_MODEL

print("API KEY:", GOOGLE_API_KEY)
print("KEY LENGTH:", len(GOOGLE_API_KEY) if GOOGLE_API_KEY else 0)

def get_embedding_model():
    return GoogleGenerativeAIEmbeddings(
        model=EMBEDDING_MODEL,
        google_api_key=GOOGLE_API_KEY
    )
