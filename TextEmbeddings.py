from langchain_community.embeddings import OllamaEmbeddings
import numpy as np

embeddings_model = OllamaEmbeddings(model="llama3")
print(f"Using embedding model: {embeddings_model.model}")
print("-" * 50)

query_text = "What is the capital of France?"
print(f"Embedding query: '{query_text}'")
query_embedding = embeddings_model.embed_query(query_text)
print(f"Query embedding length: {len(query_embedding)}")
print(f"Using embedding model: {embeddings_model.model}")
print(f"First 5 elements of query embedding: {query_embedding[:5]}\n") 
print("-" * 50)


