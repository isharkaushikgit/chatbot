import streamlit as st
import getpass
import os






import streamlit as st
from openai import OpenAI


st.title("Poem-bot")


from PIL import Image
import io
import numpy as np
import requests
image_bytes = response.content
image = Image.open(io.BytesIO(image_bytes))
image.save('output_image0.jpg')
image1 = Image.open('output_image0.jpg')
st.image(image1, caption='Enter any caption here')




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
        "you ar a poet. write a poem using the supplied word. use it atleast 2 times. 4 lines poem.",
    ),
    ("human",topic),
]



if topic:
    ai_msg = llm.invoke(messages)
    st.write(ai_msg.content)




