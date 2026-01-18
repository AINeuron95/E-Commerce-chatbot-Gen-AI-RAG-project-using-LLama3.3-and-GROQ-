import streamlit as st
from router import router
from faq import ingest_faq_data,faq_chain
from sql import sql_chain
from talk import  generate_talk_query
import os
faq_path = r"F:\Genarative AI\Project\ChatBot_RAG\E_commers_Bot\app\Resources\faq_data.csv"
ingest_faq_data(faq_path)

def ask(query):
    route = router(query).name
    if route == 'faq':
        return faq_chain(query)
    elif route == 'sql':
        return sql_chain(query)
    elif route == 'talk':
        return generate_talk_query(query)
    else:
        return f"Route {route} not implemented yet"

st.title("E Commerce Chat Bot")

query = st.chat_input("Write your query")
if "messages" not in st.session_state:
    st.session_state["messages"]=[]

for message in st.session_state.messages:
    with st.chat_message(message['role']):
        st.markdown(message['content'])



if query:
   with st.chat_message("user"):
       st.markdown(query)
   st.session_state["messages"].append({"role": "user","content":query})

   response = ask(query)
   with st.chat_message("assistant"):
       st.markdown(response)
   st.session_state["messages"].append({"role": "assistant", "content": response})

