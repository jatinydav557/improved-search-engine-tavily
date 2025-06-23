import streamlit as st
from langchain_groq import ChatGroq
from langchain_community.utilities import ArxivAPIWrapper, WikipediaAPIWrapper
from langchain_community.tools import ArxivQueryRun, WikipediaQueryRun
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain.agents import initialize_agent, AgentType
from langchain.callbacks import StreamlitCallbackHandler
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
tavily_api_key = os.getenv("TAVILY_API_KEY")

# Setup tools
arxiv_tool = ArxivQueryRun(api_wrapper=ArxivAPIWrapper(top_k_results=1, doc_content_chars_max=200))
wiki_tool = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=1000))
tavily_tool = TavilySearchResults(k=3)

# UI
st.title("🔎 LangChain - Chat with Search")
st.sidebar.title("Settings")
api_key = st.sidebar.text_input("Enter your Groq API Key:", type="password")

if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant", "content": "Hi, I'm a chatbot who can search the web using Tavily, Wikipedia, and Arxiv. How can I help you?"}
    ]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input("What's cooking up in your mind?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    llm = ChatGroq(groq_api_key=api_key, model_name="Llama3-70b-8192", streaming=True)

    agent = initialize_agent(
        tools=[tavily_tool, wiki_tool, arxiv_tool],
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
        handle_parsing_errors=True,
        agent_kwargs={
            "prefix": (
                "You are an AI assistant that can use Wikipedia, Tavily, and Arxiv tools. "
                "Only use each tool once per query unless new context is introduced. "
                "If you've already used a tool and received an answer, do not repeat the call."
            )
        }
    )

    with st.chat_message("assistant"):
        cb_handler = StreamlitCallbackHandler(st.container(), expand_new_thoughts=False)
        response = agent.run(st.session_state.messages, callbacks=[cb_handler])
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.write(response)
