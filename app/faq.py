import pandas as pd
import chromadb
from chromadb.utils import embedding_functions
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()
faq_path = r"F:\Genarative AI\Project\ChatBot_RAG\E_commers_Bot\app\Resources\faq_data.csv"
chroma_client = chromadb.Client()
collection_name_faq = 'faqs'
ef = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name = 'sentence-transformers/all-MiniLM-L6-v2',
)
groq_client = Groq()
def ingest_faq_data(path):
    #### Chromadb setup with embedding function  #####
    if collection_name_faq not in [c.name for c in chroma_client.list_collections()]:
        print('Ingesting faq data into chroma DB...')
        collection = chroma_client.get_or_create_collection(
            name=collection_name_faq,
            embedding_function=ef
        )
        #### Ingest faq data from csv file ######
        df = pd.read_csv(path)
        docs = df['question'].to_list()
        metadata = [{'answer': ans} for ans in df['answer'].to_list()]
        ids = [f"id_{i}" for i in range(len(docs))]
        ### Adding the data : question in the document and answer in metadata ###
        collection.add(
            documents=docs,
            metadatas=metadata,
            ids=ids
        )
        print(f"Added {len(docs)} documents to collection {collection_name_faq}")
    else:
        print(f"Collection {collection_name_faq} already exists")

### Get data from chromadb ###
def get_relevant_qa(query):
    collection = chroma_client.get_collection(collection_name_faq)
    result = collection.query(
        query_texts=[query],
        n_results = 2
    )
    return result

def faq_chain(query):
    result = get_relevant_qa(query)
    context = ''.join([r.get('answer') for r in result['metadatas'][0]])
    answer = generate_answer(query, context)
    return answer


def generate_answer(query, context):
    prompt = f'''Give the question and context below, generate the answer based on the context only.
    If you don't find the answer inside the context then say "I don't Know".
    Do not make things up.
    
    Question: {query}
    
    Context: {context} 
    '''
    ### Call the LLM ###
    chat_completion = groq_client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model= os.environ['GROQ_MODEL'],
        temperature=1.7,
    )
    return chat_completion.choices[0].message.content


if __name__ == "__main__" :
    # faq_df = ingest_faq_data(faq_path)
    ingest_faq_data(faq_path)
    query = "Do you take cash as a payment option ?"
    # result = get_relevant_qa(query)
    answer = faq_chain(query)
    print(answer)

    # print(faq_df)

