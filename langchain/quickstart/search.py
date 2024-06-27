"""In this tutorial we will build an agent that can interact with a search engine."""
import os
import subprocess

from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from langchain_core.tools import Tool
from langchain_google_community import GoogleSearchAPIWrapper, GoogleSearchResults
from langgraph.prebuilt import create_react_agent


# OpenAI API.
os.environ["OPENAI_API_KEY"] = subprocess.check_output(
    "security find-generic-password -s 'openai.api-key' -w", shell=True, text=True
).strip()
# Google API.
os.environ["GOOGLE_API_KEY"] = subprocess.check_output(
    "security find-generic-password -s 'google.api-key' -w", shell=True, text=True
).strip()
os.environ["GOOGLE_CSE_ID"] = subprocess.check_output(
    "security find-generic-password -s 'google.cse-id' -w", shell=True, text=True
).strip()

# search = GoogleSearchResults(num_results=2, api_wrapper=GoogleSearchAPIWrapper())
google_search = GoogleSearchResults(num_results=2, api_wrapper=GoogleSearchAPIWrapper())
search = Tool(
    name="google_search",
    description="Search Google for recent results.",
    func=google_search._run,
)
tools = [search]

model = ChatOpenAI(model="gpt-4o")
agent_executor = create_react_agent(model, tools)
response = agent_executor.invoke({"messages": [HumanMessage(content="whats the weather in sf?")]})

print(response["messages"])
