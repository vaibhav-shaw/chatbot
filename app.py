from openai import OpenAI
from dotenv import load_dotenv
import os
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

# Load environment variables from .env file
load_dotenv()

# Set environment variables for API keys
os.environ["OPENROUTER_API_KEY"] = os.getenv("OPENROUTER_API_KEY")

# Streamlit app title
st.title('Langchain ChatBot with OpenRouter Integration')

# OpenRouter client setup
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)

# Define Langchain prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Please respond to user queries."),
    ("user", "Question: {question}")
])



# OpenRouter LLM through Langchain (using OpenRouter key and model)
llm = ChatOpenAI(
    model="mattshumer/reflection-70b:free",
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

# Input text field in Streamlit UI
input_text = st.text_input("Enter your question:")

# Output parser for formatting chatbot responses
output_parser = StrOutputParser()

# Define the chain of operations to be performed on the input text
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))



# # Process the input and get a response from the chatbot
# if input_text:
#     try:
#         # Create the full prompt using the template and user input
#         prompt = prompt.format(question=input_text)

#         # Chain the prompt to the LLM and parse the output
#         response = llm(prompt)
#         parsed_output = output_parser.parse(response)
        
#         # Display the output
#         st.write(parsed_output.content)

#     except Exception as e:
#         st.error(f"An error occurred: {e}")
