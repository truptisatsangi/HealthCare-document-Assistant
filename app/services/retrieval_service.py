from typing import Optional

from langchain_core.documents import Document
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings


class RetrievalService:
    """
    Responsible for retrieving relevant documents from the vector database.

    Responsibilities:
    - Embed the user query.
    - Perform similarity search.
    - Apply metadata filters.
    - Return the Top-K relevant chunks.
    """

    def __init__(self, persist_directory: str = "./chroma_db", top_k: int = 5):
        self.embedding_model = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-mpnet-base-v2",
            encode_kwargs={"normalize_embeddings": True},
        )

        self.vector_store = Chroma(
            collection_name="medical_reports",
            embedding_function=self.embedding_model,
            persist_directory=persist_directory,
        )

        self.top_k = top_k

    def retrieve(
        self,
        query: str,
        filter: Optional[dict] = None,
    ) -> list[Document]:
        
        # Chroma.similarity_search() embed query internally using the embedding_function passed during initialization.
        documents = self.vector_store.similarity_search(
            query=query,
            k=self.top_k,
            filter=filter,
        )

        return documents