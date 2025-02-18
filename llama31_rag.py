from langchain_community.vectorstores import Chroma
from langchain_community.chat_models import ChatOllama
from langchain_community.embeddings import FastEmbedEmbeddings
from langchain.schema.output_parser import StrOutputParser
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema.runnable import RunnablePassthrough
from langchain.prompts import PromptTemplate
from langchain.vectorstores.utils import filter_complex_metadata
#from langchain_openai import OpenAIEmbeddings

class ChatPDF:
    vector_store = None
    retriever = None
    chain = None

    def __init__(self):
        self.model = ChatOllama(model="llama3.1:8b",temperature=0,)

        self.text_splitter = RecursiveCharacterTextSplitter(chunk_size=2000, chunk_overlap=250)
        
        self.prompt = PromptTemplate(
            template="""You are an assistant in multifunctional tasks related to text analysis. 
            
            Use the context below to answer the question.
            
            If you don't know the answer, just say that you don't know. 
            
            In your answer, include information about the name of the document and the page where you can find the information that was the basis for the answer.
            
            Write a detailed and concise answer:
            Question: {question} 
            Context: {context} 
            Answer: 
            """,
            input_variables=["question"],
        )
        

    def ingest(self, pdf_file_path: str):
        docs = PyPDFLoader(file_path=pdf_file_path).load()
        chunks = self.text_splitter.split_documents(docs)
        chunks = filter_complex_metadata(chunks)

        vector_store = Chroma.from_documents(documents=chunks, embedding=FastEmbedEmbeddings())

        self.retriever = vector_store.as_retriever(k=4)

        self.chain = ({"context": self.retriever, "question": RunnablePassthrough()}
                      | self.prompt
                      | self.model
                      | StrOutputParser())

    def ask(self, query: str):
        if not self.chain:
            return "Please, add a PDF document first."

        return self.chain.invoke(query)

    def clear(self):
        self.vector_store = None
        self.retriever = None
        self.chain = None