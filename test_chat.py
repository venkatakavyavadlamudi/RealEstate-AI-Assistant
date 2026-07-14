from rag.chat_engine import ChatEngine


chat = ChatEngine()


question = "What is the possession date of Urban Nest Riverside?"


result = chat.ask(question)


print("\nQuestion:")
print(result["question"])


print("\nAnswer:")
print(result["answer"])


print("\nSources:")
print(result["sources"])
