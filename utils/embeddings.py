from langchain.embeddings import OllamaEmbeddings
def embeddings_mg (chunks):
    ollama_emb = OllamaEmbeddings( model="nomic-embed-text")  
    embeddings= ollama_emb.embed_documents
    return embeddings
