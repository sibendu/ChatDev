import os
from openai import AzureOpenAI
#from langchain_openai import AzureOpenAI
#from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage

os.environ["OPENAI_API_VERSION"] = "2023-07-01-preview"
os.environ["AZURE_OPENAI_ENDPOINT"] = "https://it-dce-openai-assistant-useast2.openai.azure.com/"
os.environ["AZURE_OPENAI_API_KEY"] = "4c47958493254eccba0c480c2f8de157"

messages = [
    SystemMessage(content="You're a helpful assistant"),
    HumanMessage(content="What is the purpose of model regularization?"),
]
client = AzureOpenAI(
            api_key = os.getenv("OPENAI_API_KEY"),
            api_version = os.getenv("OPENAI_API_VERSION"),
            azure_endpoint = os.getenv("OPENAI_API_BASE"),
    )
response = client.chat.completions.create(
    model="gpt-35-turbo-16k",
    messages=messages)

print(response)