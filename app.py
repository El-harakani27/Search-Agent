from langchain_community.tools import ArxivQueryRun,WikipediaQueryRun,DuckDuckGoSearchRun
from langchain_community.utilities import ArxivAPIWrapper,WikipediaAPIWrapper
from langchain_groq import ChatGroq
from langchain.agents import initialize_agent,AgentType
from langchain.callbacks import StreamlitCallbackHandler
import streamlit as st
import os


arxiv_wrapper = ArxivAPIWrapper(top_k_results=1,doc_content_chars_max=200)
arxiv = ArxivQueryRun(api_wrapper=arxiv_wrapper)

wiki_wrapper = WikipediaAPIWrapper(top_k_results=1,doc_content_chars_max=200)
wiki = WikipediaQueryRun(api_wrapper=wiki_wrapper)

search = DuckDuckGoSearchRun(name='Seach')


st.title('LangChain - Chat with search')

st.sidebar.title("Settings")
GROQ_API = st.sidebar.text_input('Enter your Groq API Key:',type='password')

if 'messages' not in st.session_state:
    st.session_state['messages'] = [
        {'role':'assistant','content':"Hi,I'm a chatbot who can search the web.How can i help you ?"}
    ]
for msg in st.session_state['messages']:
    st.chat_message(msg['role']).write(msg['content'])
if prompt:=st.chat_input(placeholder='What is Machine learning?'):
    st.session_state['messages'].append({'role':'user','content':prompt})
    st.chat_message("user").write(prompt)
    llm = ChatGroq(api_key=GROQ_API,
                   model="Llama3-8b-8192")
    tools = [arxiv,wiki,search]
    seach_agent = initialize_agent(tools=tools,agent=AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION,llm=llm,handling_parsing_errors =True)
    with st.chat_message('assistant'):
        st_cb = StreamlitCallbackHandler(st.container(),expand_new_thoughts=False)
        response = seach_agent.run(st.session_state.messages,callbacks=[st_cb])
        st.session_state.messages.append({'role':'assistant','content':response})
        st.write(response)