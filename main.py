# borrowed from https://github.com/streamlit/llm-examples/blob/main/pages/2_Langchain_Quickstart.py
import json
import urllib
import streamlit as st
from langchain import OpenAI
from oai_utils import get_openai_api_key

PROMPTS_CACHE = "prompts.json"
MAX_PROMPT_HISTORY = 10

def get_prompts():
    try:
        with open(PROMPTS_CACHE, 'r') as fin:
            return json.load(fin)
    except FileNotFoundError:
        return []


def render_prompt(prompt):
    quoted = urllib.parse.quote_plus(prompt, safe='')
    url = f"?prompt={quoted}"        
    st.sidebar.markdown(f" * [{prompt}]({url})")
    

def add_prompt(prompts, new_prompt):
    if new_prompt not in prompts:
        prompts = [new_prompt] + prompts
        prompts = prompts[:MAX_PROMPT_HISTORY]
        render_prompt(new_prompt)
        with open(PROMPTS_CACHE, 'w') as fout:
            json.dump(prompts, fout)


openai_api_key = get_openai_api_key()

def generate_response(input_text, model_name):
    llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key, model_name=model_name)
    st.info(llm(input_text))


st.markdown("# LLM Notebook")
st.sidebar.markdown("# Prompts")
prompts = get_prompts()
for prompt in prompts:
    render_prompt(prompt)


with st.form('my_form'):
    oai_model = st.selectbox(
        'Which OpenAI model should we use?',
        ('gpt-3.5-turbo', 'gpt-4', 'ada', 'babbage', 'curie', 'davinci'),
    )

    prompt = ''
    params = st.experimental_get_query_params()
    if 'prompt' in params:
        prompt = params['prompt'][0]
    
    text = st.text_area('Prompt:', prompt, placeholder='How do I use Streamlit to query OpenAI?')
    submitted = st.form_submit_button('Submit')
    if submitted:
        add_prompt(prompts, text)
        generate_response(text, oai_model)

