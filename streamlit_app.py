import streamlit as st
import getpass
import os

st.write("dkdkdkdy")


os.environ["OPENAI_API_KEY"]='os.environ["OPENAI_API_KEY"]='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''
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

