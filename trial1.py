import os
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory
from langchain.chains import SequentialChain
from langchain.prompts import PromptTemplate

from decouple import config
from dotenv import load_dotenv

import streamlit as st

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")

st.title("Person Info")
input_text = st.text_input("Write any famous person name.")

# prompt templates
first_input_prompt = PromptTemplate(
    input_variables=['name'],
    template="Tell me about {name}"
)
