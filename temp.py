# from langchain_ollama import OllamaLLM

# model = OllamaLLM(model="gemma2:2b")

# results = model.invoke(input="Hello World")
# print(results)

# from langchain_ollama import OllamaLLM
# from langchain_core.prompts import ChatPromptTemplate

# template = """
# Answer the question below.

# Here is the conversation history : {context}

# Questions : {questions}
# Answer :
# """

# model = OllamaLLM(model = "gemma2:2b")
# prompt = ChatPromptTemplate.from_template(template)
# chain = prompt | model

# results = chain.invoke({"context" : "","questions" : "Hey How are you"})
# print(results)


# PART 3 STORING THE CONVERSATION HISTORY

from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template = """
Answer the question below.

Here is the conversation history : {context}

Questions : {questions}
Answer :
"""

model = OllamaLLM(model="gemma2:2b")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model


def handle_conversation():
    context = ""
    print("Welcome to the AI chatbot ! Type 'exit' to quit.")
    while True:
        user_input = input("You : ")
        if user_input.lower() == "exit":
            break

        results = chain.invoke({"context": context, "questions": user_input})
        print("Bot : ",results)
        context += f"\n User : {user_input}\n AI : {results}"

if __name__ =="__main__":
    handle_conversation()