from langchain_core.output_parsers import StrOutputParser
from langchain_core.language_models.chat_models import BaseChatModel
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables.base import RunnableSequence


def get_chain(model: BaseChatModel) -> RunnableSequence:
    """Get translator chain."""
    system_template = "Translate the following into {language}:"
    prompt_template = ChatPromptTemplate.from_messages(
        [("system", system_template), ("user", "{text}")]
    )
    parser = StrOutputParser()
    chain = prompt_template | model | parser
    return chain
