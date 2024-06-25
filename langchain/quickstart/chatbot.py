"""This chatbot will be able to have a conversation and remember previous interactions.

There are several other related concepts that you may be looking for:
- Conversational RAG: Enable a chatbot experience over an external source of data
- Agents: Build a chatbot that can take actions

This tutorial will cover the basics which will be helpful for those two more advanced topics.
"""
import os
import subprocess

from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage


# Get OpenAI model.
os.environ["OPENAI_API_KEY"] = subprocess.check_output(
    "security find-generic-password -s 'api-key.openai' -w", shell=True, text=True
).strip()

model = ChatOpenAI(model="gpt-4o")
response = model.invoke([HumanMessage(content="Hi! I'm Bob")])
print(response)
