from langchain_core.documents import Document
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma


class EmbeddingService:
    """
    Responsible for generating embeddings and storing them in the vector database.

    Responsibilities:
    - Initialize embedding model.
    - Convert chunks into embeddings.
    - Store embeddings in Chroma.
    """

    def __init__(self, persist_directory: str = "./chroma_db"):
        self.embedding_model = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-mpnet-base-v2",
            encode_kwargs={"normalize_embeddings": True},
        )

        self.vector_store = Chroma(
            collection_name="medical_reports",
            embedding_function=self.embedding_model,
            persist_directory=persist_directory,
        )

    def store_embeddings(self, chunks: list[Document]) -> list[str]:
        document_ids = self.vector_store.add_documents(chunks)

        return document_ids