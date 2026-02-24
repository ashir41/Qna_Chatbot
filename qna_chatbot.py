## LLm
##Tool-google search tool
##Agent
##memory
##streaming
##web interface

from dotenv import load_dotenv
load_dotenv()

from langchain_groq import ChatGroq
from langchain_community.utilities import GoogleSerperAPIWrapper
from langchain.agents import create_agent
from langgraph.checkpoint.memory import InMemorySaver
import streamlit as st

llm=ChatGroq(model="openai/gpt-oss-20b", streaming=True)
search=GoogleSerperAPIWrapper()
tools= [search.run]
    
if "memory" not in st.session_state:
    st.session_state.memory= InMemorySaver()
    st.session_state.history=[]


agent= create_agent(
    model= llm, 
    tools=tools, 
    checkpointer=st.session_state.memory,
    system_prompt="You are amazing assistant that helps answer questions using google search."
    )
print(st.session_state.memory)
###web interface
st.subheader("QnA Chatbot with Groq and Google Search")
for message in st.session_state.history:
    role= message["role"]
    content= message["content"]
    st.chat_message(role).markdown(content)

query= st.chat_input("Ask a question:")
if query:
    st.chat_message("user").markdown(query)
    st.session_state.history.append({"role": "user", "content": query})
    response= agent.stream(
        {"messages": [{"role": "user", "content": query}]},
        {"configurable": {"thread_id": "1"}},
        stream_mode="messages"
    )
    ai_container= st.chat_message("ai")
    with ai_container:
        space = st.empty()
        message = ""
        for chunk in response:
            message+=chunk[0].content
            space.write(message)
    
        st.session_state.history.append({"role": "ai", "content": message})
