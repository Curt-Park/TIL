import os
import subprocess

import translator

from fastapi import FastAPI
from langserve import add_routes


# Get OpenAI model.
os.environ["OPENAI_API_KEY"] = subprocess.check_output(
    "security find-generic-password -s 'api-key.openai' -w", shell=True, text=True
).strip()


# App definition
app = FastAPI(
    title="LangChain Server",
    version="1.0",
    description="A simple API server using LangChain's Runnable interfaces",
)

# Adding chain route
add_routes(
    app,
    translator.chain,
    path="/translate",
)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)
