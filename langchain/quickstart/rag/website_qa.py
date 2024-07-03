import os
import subprocess

import bs4
from langchain import hub
from langchain_chroma import Chroma
from langchain_community.document_loaders import WebBaseLoader
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

# OpenAI API.
os.environ["OPENAI_API_KEY"] = subprocess.check_output(
    "security find-generic-password -s 'openai.api-key' -w", shell=True, text=True
).strip()

llm = ChatOpenAI(model="gpt-4o")

# Load, chunk and index the contents of the blog.
loader = WebBaseLoader(
    web_paths=("https://lilianweng.github.io/posts/2023-06-23-agent/",),
    bs_kwargs=dict(
        parse_only=bs4.SoupStrainer(
            class_=("post-content", "post-title", "post-header")
        )
    ),
)
docs = loader.load()

# https://python.langchain.com/v0.1/docs/modules/data_connection/document_transformers/recursive_text_splitter/
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
splits = text_splitter.split_documents(docs)
vectorstore = Chroma.from_documents(documents=splits, embedding=OpenAIEmbeddings())

# Retrieve and generate using the relevant snippets of the blog.
retriever = vectorstore.as_retriever()
prompt = hub.pull("rlm/rag-prompt")
print("prompt:", prompt)
print()
print("retriever:", retriever)
print()


def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)


# format_docs is cast to a RunnableLambda.
# "context" and "question" is cast to a RunnableParallel.
rag_chain = (
    {
        # retriever | format_docs passes the question through the retriever, generating Document objects,
        # and then to format_docs to generate strings;
        "context": retriever | format_docs,
        # RunnablePassthrough() passes through the input question unchanged.
        "question": RunnablePassthrough(),
    }
    | prompt
    | llm
    | StrOutputParser()
)
result = rag_chain.invoke("What is Task Decomposition?")
print("result:", result)


# Cleanup.
vectorstore.delete_collection()
