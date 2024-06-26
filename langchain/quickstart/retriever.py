"""This tutorial will familiarize you with LangChain's vector store and retriever abstractions."""
from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_core.language_models.chat_models import BaseChatModel
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda, RunnablePassthrough
from langchain_core.runnables.base import Runnable
from langchain_openai import OpenAIEmbeddings


# Sample documents.
documents = [
    Document(
        page_content="Dogs are great companions, known for their loyalty and friendliness.",
        metadata={"source": "mammal-pets-doc"},
    ),
    Document(
        page_content="Cats are independent pets that often enjoy their own space.",
        metadata={"source": "mammal-pets-doc"},
    ),
    Document(
        page_content="Goldfish are popular pets for beginners, requiring relatively simple care.",
        metadata={"source": "fish-pets-doc"},
    ),
    Document(
        page_content="Parrots are intelligent birds capable of mimicking human speech.",
        metadata={"source": "bird-pets-doc"},
    ),
    Document(
        page_content="Rabbits are social animals that need plenty of space to hop around.",
        metadata={"source": "mammal-pets-doc"},
    ),
]


def get_chain(model: BaseChatModel) -> Runnable:
    """Get retriever chain."""
    # Instantiate an in-memory vector store.
    vectorstore = Chroma.from_documents(
        documents,
        embedding=OpenAIEmbeddings(),
    )
    # Bind with Runnable for chaining.
    retriever = RunnableLambda(vectorstore.asimilarity_search).bind(k=1)

    system_template = "Answer this question using the provided context only."
    context_template = "Context:\n{context}"
    prompt_template = ChatPromptTemplate.from_messages(
        [("system", system_template), ("user", "{question}"), ("system", context_template)]
    )
    parser = StrOutputParser()
    rag_chain = (
        {"context": retriever, "question": RunnablePassthrough()}
        | prompt_template
        | model
        | parser
    )
    return rag_chain
