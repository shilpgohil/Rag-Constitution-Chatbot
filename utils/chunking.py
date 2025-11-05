from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.load import load
import BeautifulSoaps
def chunkings_mg(db_url="url",str):
    chn= BeautifulSoaps("url")
    chn_store= chn.load()
    splitter= RecursiveCharacterTextSplitter(chunk_size= 400, chunk_overlap=60 )
    chunks= splitter(chn_store)
    return chunks