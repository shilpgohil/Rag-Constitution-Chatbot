# RAG Chatbot
The overall Objective of the project is to built Converssational RAG Chatbot that answers multi turn questions about the indian constitution, hearning and laws

## Installation Guide 
-TechStack used python 3.8. So for quick setup follow the below steps:
1. **Clone the repository**:
    ```bash
    git clone <the_repository_link>
    ```

2. **Install dependencies**:
    If you have a `requirements.txt` file, install the necessary libraries:
    ```bash
    pip install -r requirements.txt
    ```

3. **Set up the environment (if needed)**:
    here we need specific Environment to setup as we are supposed to use the LLM API in the file ".env" (in the present case we are using Ollama api)

## Running the Application
Run the application using the following command:
    ```bash
    python app.py
    ```
## File Structure
```
│── app.py  #Fastapi app along with the /askme endpoint also get integrations usiong beautifulsoup4 from the external sources like kesavandanda bharti, menka gandhi etc.,
│── main.py  #the main app the retrives the whole pipeline and used mainly for testing
│── requirements.txt  #here arre the basis dependencies that will help to execute the project successfully
│── utils/
│   ├── chunking.py  #at this section we  innitiate the pipeline by mapping the retrieval document loaction using beautifulsoup4 from the source and assigning the chunk rules using RecursiveCharacterTextSplitter as mentioned below. here the chunk size= 400, chunk overlap=60
│   ├── embeddings.py  # for a successful chunnking of an document it need to undergo a fine embedding process here in this algorithm the embedding model the we have used is "nomic-emnd-text" which allows us a pretty decent amount of dimensions in the vectore database something around 310 to 312 and the vector database we have used is ChromaDB
│   ├── retrievals.py  # at this section of the project we are enabeling the chunks to further undergo its destination which further allows retriever to aggregate from the destinatiion and return the retrieve the Top k where k is assigned 3,  so the retriever will pass the most revelent chunk from all the top 3 called chuks
│   ├── llm.py #here is where the whole brainroobeapart is setelled up along with the model used to query passed and the subject prompt so the the agent knows what when and how to behave and return the response also the llm have the multilingual freedom to underdtand as well as response in hindi
│   ├── __pychache__/
│   ├── ├── chunking.cpython-310.pyc 
```
--

* For the above project used Ollama as the LLM:model used is "llama3.2"
* Along with the temperature as= 0.5 (to keep the llm creative as well as deterministic to the objective) we can also use temperature as 0, 1 or more than 1 but in case of 0 the llm will be bounded and stay sharp to its knowledge base and in terms of assigning parameter 1 or more than 1 it will dive more into generating creative reponses. Therefore to keep the model relatively Converssational as well as smart at its responses i metained the parameter as 0.5
* The embedding model used here is: "nomic-embed-text" yet it allows a good amount of dimensions with in the vector data
* For chunking i have used the RecursiceCharacterTextSplitter from langchain TectSplitter which uses the chunking stretergy for first it will chunk paragraph (\n\n), followed by lines (\n), gramatical breaks (,.!etc), than comes words, semi words (tricolour= 'tri','colour') and than try symmentically to immplement self attention in terms or retrievals
