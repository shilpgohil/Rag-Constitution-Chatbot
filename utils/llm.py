from langchain.chat_models import ollama
from langchain.chains import retrieval_qa
def llm_mg(query: str, retriever):
    chat_model= ollama(model="llama3.2:3b", temperature=0)
    subject_prompt= ("you are a conversational Chatbot, respnsible to answer the about the Indian Constitution, hearing and laws")
    qa_chain= retrieval_qa.from_chain_type(llm=chat_model,
                                           chain_type=(subject_prompt,"stuff"), 
                                           retriever=retriever, 
                                           return_source_doc=False)
    answer= qa_chain.run(query)
    return answer