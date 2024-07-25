from langchain_ollama import ChatOllama
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st

'''
prompt = PromptTemplate(
    template="""You are an assistant for question-answering tasks. 
    
    Use the following documents to answer the question. 
    
    If you don't know the answer, just say that you don't know. 
    
    Use three sentences maximum and keep the answer concise:
    Question: {question} 
    Documents: {documents} 
    Answer: 
    """,
    input_variables=["question", "documents"],
)
'''

prompt = PromptTemplate(
    template="""You are an assistant for question-answering tasks. 
    
    If you don't know the answer, just say that you don't know. 
    
    Use three sentences maximum and keep the answer concise but be ready to give an in depth explanation if asked for:
    Question: {question} 
    Answer: 
    """,
    input_variables=["question"],
)

# Set up the Streamlit framework
st.title('Langchain Chatbot With llama3.1:8b model')  # Set the title of the Streamlit app
input_text=st.text_input("Ask your question!")  # Create a text input field in the Streamlit app

# Initialize the Ollama model
llm = ChatOllama(
    model="llama3.1:latest",
    temperature=0,
)

rag_chain = prompt | llm | StrOutputParser()

if input_text:
    st.write(rag_chain.invoke({"question":input_text}))