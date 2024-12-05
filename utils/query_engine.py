# utils/query_engine.py

from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, StorageContext, load_index_from_storage

def build_index(directory_path):
    """
    Build a vector store index from documents in a directory.

    Args:
        directory_path (str): Path to the directory containing documents.

    Returns:
        VectorStoreIndex: The built index.
    """
    documents = SimpleDirectoryReader(directory_path).load_data()
    index = VectorStoreIndex.from_documents(documents)
    index.storage_context.persist(persist_dir="data/index")
    return index

def query_index(query):
    """
    Query the vector store index.

    Args:
        query (str): The query string.

    Returns:
        str: The query response.
    """
    storage_context = StorageContext.from_defaults(persist_dir="data/index")
    index = load_index_from_storage(storage_context)
    response = index.as_query_engine(streaming=True).query(query)
    return str(response)
