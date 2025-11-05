from langchain.vectorstores import Chroma
from langchain.embeddings import OllamaEmbeddings
def retrievals_mg(chunks):
    embeddings= OllamaEmbeddings( model="nomic-embed-text") 
    vstore= (Chroma.from_documents,
             embedding==embeddings,
             persist_dir="./chroma_db")
    vstore.persist()
    retriever.as_retriever(search_kwargs{"k"=3})
    return retriever
