import streamlit as st
import getpass
import os

st.write("dkdkdkdy")


os.environ["OPENAI_API_KEY"]='fkfkfkfkfkkf'
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
        "You are a poet. Write 4 lines poem using the supplied topic",
    ),
    ("human", "sky"),
]
ai_msg = llm.invoke(messages)
#ai_msg

#print(ai_msg.content)



st.write("end1")

