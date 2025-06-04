import streamlit as st
import getpass
import os


#st.write("dkdkdkdy")
#st.write(st.secrets.get("open_api_key"))
#os.environ["OPENAI_API_KEY"]=st.secrets.get("open_api_key")




import streamlit as st
from openai import OpenAI

# Show title and description.
st.title("💬 Chatbott")
#openai_api_key = st.text_input("OpenAI API Key", type="password")





openai_api_key = st.secrets.get("open_api_key")
topic = st.text_input("topic pleasee")

if topic:
    import getpass
    import os
    
    os.environ["OPENAI_API_KEY"]=openai_api_key
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
        ("human", topic),
    ]
    ai_msg = llm.invoke(messages)
    st.write(ai_msg.content)




