import streamlit as st
import getpass
import os






import streamlit as st
from openai import OpenAI


st.title("Poem-bot")






openai_api_key = st.secrets.get("open_api_key")
os.environ["OPENAI_API_KEY"]=openai_api_key
topic = st.text_input("topic pleasee")

import getpass
import os
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="gpt-4o",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    # api_key="...",  # if you prefer to pass api key in directly instaed of using env vars
    # base_url="...",
    # organization="...",
    # other params...
)

messages = [
    (
        "system",
        "You are a poet. Write 4 lines poem using the supplied topic. Use the word twice.",
    ),
    ("human",topic),
]

if topic:

    ai_msg = llm.invoke(messages)
    st.write(ai_msg.content)




