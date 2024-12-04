# utils/query_engine.py

from llama_index import GPTVectorStoreIndex, SimpleDirectoryReader
import os

def build_index(documents_dir):
    """
    Builds an index over the documents for querying.

    Args:
        documents_dir (str): Directory containing document text files.
    """
    documents = SimpleDirectoryReader(documents_dir).load_data()
    index = GPTVectorStoreIndex.from_documents(documents)
    index.save_to_disk('data/index.json')

def query_index(query):
    """
    Queries the index and returns an answer.

    Args:
        query (str): The user's question.

    Returns:
        str: The answer from the LLM.
    """
    index = GPTVectorStoreIndex.load_from_disk('data/index.json')
    response = index.query(query)
    return response
