import os
# from langchain.vectorstores.pinecone import Pinecone
from pinecone import Pinecone
from langchain_pinecone import PineconeVectorStore as PineconeLC
from app.chat.embeddings.openai import embeddings

pc = Pinecone(
    api_key=os.getenv("PINECONE_API_KEY")     
)

vector_store = PineconeLC(
    index=pc.Index(name=os.getenv("PINECONE_INDEX_NAME")),
    embedding=embeddings,
    text_key="text"
)