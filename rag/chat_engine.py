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

        self.chat_history = []


    def ask(self, question):

        # Retrieve relevant documents
        documents = self.retriever.retrieve(question)


        # Create document context
        context = "\n\n".join(
            [
                doc.page_content
                for doc in documents
            ]
        )


        # Get previous conversation
        history = "\n".join(
            self.chat_history[-6:]
        )


        # Combine memory + retrieved documents
        combined_context = f"""
Previous Conversation:
{history}

Retrieved Documents:
{context}
"""


        # Create prompt
        prompt = RAG_PROMPT.format(
            history=history,
            context=combined_context,
            question=question
        )


        # Generate response
        response = self.llm.invoke(prompt)

        answer = response.content


        # Gemini response handling
        if isinstance(answer, list):
            answer = answer[0]["text"]


        # Save conversation
        self.chat_history.append(
            f"User: {question}"
        )

        self.chat_history.append(
            f"Assistant: {answer}"
        )


        return {
            "question": question,
            "answer": answer,
            "sources": [
                doc.metadata
                for doc in documents
            ]
        }


    def clear_history(self):

        self.chat_history = []
