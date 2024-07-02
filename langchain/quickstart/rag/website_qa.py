import os
import subprocess

from langchain_openai import ChatOpenAI


# OpenAI API.
os.environ["OPENAI_API_KEY"] = subprocess.check_output(
    "security find-generic-password -s 'openai.api-key' -w", shell=True, text=True
).strip()


llm = ChatOpenAI(model="gpt-4o")
