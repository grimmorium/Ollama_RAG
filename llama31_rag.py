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
        self.model = ChatOllama(model="llama3.1:latest",temperature=0,)

        self.text_splitter = RecursiveCharacterTextSplitter(chunk_size=250, chunk_overlap=0)
        #self.prompt = PromptTemplate.from_template(
        #    """
        #    <s> [INST] This is a chat between a user and an artificial intelligence assistant. The assistant gives helpful, detailed, and polite answers to the user’s questions based on the context. The assistant should also indicate when the answer cannot be found in the context. [/INST] </s> 
        #    [INST] Question: {question} 
        #    Context: {context} 
        #    Answer: [/INST]
        #    """
        #)
        '''
        self.prompt = PromptTemplate.from_template(
            """
            {{ if .System }}System: {{ .System }}

            {{ end }}{{ if .Prompt }}User: {{ .Prompt }}

            {{ end }}Assistant: <|begin_of_text|>{{ .Response }}
            """
        )
        '''
        self.prompt = PromptTemplate(
            template="""You are an assistant for question-answering tasks. 
            
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
        #vector_store = Chroma.from_documents(documents=chunks, embedding=OpenAIEmbeddings())
        
        '''
        self.retriever = vector_store.as_retriever(
            search_type="similarity_score_threshold",
            search_kwargs={
                "k": 3,
                "score_threshold": 0.5,
            },
        )
        '''
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