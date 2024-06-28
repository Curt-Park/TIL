"""Langchain server for quickstart examples."""

import argparse
import os
import subprocess

from fastapi import FastAPI
from langchain_openai import ChatOpenAI
from langserve import add_routes

import chatbot
import retriever
import translator

parser = argparse.ArgumentParser()
parser.add_argument("-m", "--model", type=str, default="gpt-4o")
args = parser.parse_args()


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

# Create model
model = ChatOpenAI(model=args.model)

# App definition
app = FastAPI(
    title="LangChain Server",
    version="1.0",
    description="A simple API server using LangChain's Runnable interfaces",
)

# Adding chain routes
add_routes(
    app,
    translator.get_chain(model),
    path="/translate",
)
add_routes(
    app,
    chatbot.get_chain(model),
    per_req_config_modifier=chatbot.per_request_config_modifier,
    path="/chat",
    # Disable playground and batch
    # 1) Playground we're passing information via headers, which is not supported via
    #    the playground right now.
    # 2) Disable batch to avoid users being confused. Batch will work fine
    #    as long as users invoke it with multiple configs appropriately, but
    #    without validation users are likely going to forget to do that.
    #    In addition, there's likely little sense in support batch for a chatbot.
    disabled_endpoints=["playground", "batch"],
)
add_routes(
    app,
    retriever.get_chain(model),
    path="/retriever",
)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)
