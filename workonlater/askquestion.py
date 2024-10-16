import openai
from openai import OpenAI
import os
from dotenv import load_dotenv



# Load environment variables from the .env file
load_dotenv(dotenv_path='')
csv_directory = ''

# Set up your OpenAI API key from the environment variable
openai.api_key= os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=openai.api_key)


# Define the function to ask a question to ChatGPT
def ask_gpt(question):
    completion = openai.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "user",
            "content": "Say this is a test",
        },
    ],
)

    return completion['choices'][0]['message']['content']




