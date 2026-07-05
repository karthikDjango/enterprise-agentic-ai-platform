from services.rag_service import rag_search

question = input("Question: ")

answer = rag_search(question)

print("\nAnswer:\n")
print(answer)