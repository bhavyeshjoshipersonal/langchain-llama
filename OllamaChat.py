import langchain
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.chat_models import ChatOllama


llm = ChatOllama(model="llama3", temperature=0)
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful AI assistant. Answer the user's questions concisely."),
        ("human", "{input}"),
    ]
)

chain = prompt | llm | StrOutputParser()


question1 = "What is the capital of France?"
print(f"User: {question1}")
answer1 = chain.invoke({"input": question1})
print(f"AI: {answer1}")

question2 = "Tell me a fun fact about giraffes."
print(f"User: {question2}")
answer2 = chain.invoke({"input": question2})
print(f"AI: {answer2}")

question3 = "What day comes after Friday?"
print(f"User: {question3}")
answer3 = chain.invoke({"input": question3})
print(f"AI: {answer3}")

question4 = "I like tomatoes, what should I eat?"
print(f"User: {question4}")
answer4 = chain.invoke({"input": question4})
print(f"AI: {answer4}")