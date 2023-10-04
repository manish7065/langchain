import os
from langchain.llms import OpenAI
from decouple import config
import streamlit as st
from dotenv import load_dotenv

# Load environment variables from the .env file into the local environment
load_dotenv()


openai_api_key  = config('OPENAI_API_KEY')
# os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY



st.title('Langchain Demo with OPENAI API')
input_text = st.text_input("Ask any question")

## LLM

llm = OpenAI(temperature=0.6)


if input_text:
    st.write(llm(input_text))