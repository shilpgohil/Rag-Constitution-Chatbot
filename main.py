from dotenv import load_dotenv
import os
from utils.chunking import chunkings_mg
from utils.retrievals import retrievals_mg
from utils.llm import  llm_mg
def main():
    load_dotenv()
    ai_api= os.getenv("my Ollama api")
    chunks = chunkings_mg("db_url")
    retriver = retrieval_mg(chunks)
    query = input("\n ask me")
    answer = llm_mg(query, retriver)
    print("\n", answer)
    
if __name__=="__main__":
    main()
