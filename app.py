from dotenv import load_dotenv
import os
from fastapi import FastAPI
from utils.chunking import chunkings_mg
from utils.retrievals import retrievals_mg
from utils.llm import llm_mg

app = FastAPI(title="RAG assignment FastAPI", version="0.1")
app.include_router(router, prefix="/api")
load_dotenv()
ai_api= os.getenv("my Ollama api")
chunks = chunkings_mg("db_url")
retriver = retrieval_mg(chunks)
query = input("\n ask me")
answer = llm_mg(query, retriver)
print("\n", answer)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8002, reload=True)