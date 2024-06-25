"""Langchain server for quickstart examples."""
import argparse
import os
import subprocess

import translator

from fastapi import FastAPI
from langchain_openai import ChatOpenAI
from langserve import add_routes


parser = argparse.ArgumentParser()
parser.add_argument("-m", "--model", type=str, default="gpt-4o")
args = parser.parse_args()


# Get OpenAI model.
os.environ["OPENAI_API_KEY"] = subprocess.check_output(
    "security find-generic-password -s 'api-key.openai' -w", shell=True, text=True
).strip()

# Create model
model = ChatOpenAI(model=args.model)

# App definition
app = FastAPI(
    title="LangChain Server",
    version="1.0",
    description="A simple API server using LangChain's Runnable interfaces",
)

# Adding chain route
add_routes(
    app,
    translator.get_chain(model),
    path="/translate",
)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)
