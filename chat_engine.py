from langchain_google_genai import ChatGoogleGenerativeAI

from rag.retriever import Retriever
from rag.prompt import RAG_PROMPT

from utils.config import LLM_MODEL


class ChatEngine:

    def __init__(self):

        self.retriever = Retriever()

        self.llm = ChatGoogleGenerativeAI(
            model=LLM_MODEL,
            temperature=0.2
        )

    def ask(self, question):

        # Retrieve relevant documents
        documents = self.retriever.retrieve(question)

        # Build context
        context = "\n\n".join(
            doc.page_content
            for doc in documents
        )

        # Create prompt
        prompt = RAG_PROMPT.format(
            context=context,
            question=question
        )

        # Generate answer
        response = self.llm.invoke(prompt)

        answer = response.content

        # Gemini may return a list instead of a string
        if isinstance(answer, list):
            answer = answer[0]["text"]

        # Collect unique source file names
        sources = []

        for doc in documents:
            source = doc.metadata.get("source", "Unknown")
            if source not in sources:
                sources.append(source)

        return {
            "question": question,
            "answer": answer,
            "sources": sources
        }
