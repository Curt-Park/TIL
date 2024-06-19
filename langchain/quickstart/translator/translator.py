import os
import subprocess

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

# Get OpenAI model.
os.environ["OPENAI_API_KEY"] = subprocess.check_output(
    "security find-generic-password -s 'api-key.openai' -w", shell=True, text=True
).strip()
model = ChatOpenAI(model="gpt-4o")

# Prompt Templates.
system_template = "Translate the following into {language}:"
prompt_template = ChatPromptTemplate.from_messages(
    [("system", system_template), ("user", "{text}")]
)

# Chain model and parser.
parser = StrOutputParser()
chain = prompt_template | model | parser

# Send the query.
result = chain.invoke({"language": "korean", "text": "hi"})
print(result)
