# borrowed from https://github.com/streamlit/llm-examples/blob/main/pages/2_Langchain_Quickstart.py
import streamlit as st
from langchain import OpenAI
from oai_utils import get_openai_api_key


openai_api_key = get_openai_api_key()


def generate_response(input_text):
    llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
    st.info(llm(input_text))


st.markdown("# LLM Notebook")
st.sidebar.markdown("# LLM Notebook")


with st.form('my_form'):
    text = st.text_area('Prompt:', '', placeholder='How do I use Streamlit to query OpenAI?')
    submitted = st.form_submit_button('Submit')
    if submitted:
        generate_response(text)

