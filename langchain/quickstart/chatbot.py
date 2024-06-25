"""This chatbot will be able to have a conversation and remember previous interactions.

There are several other related concepts that you may be looking for:
- Conversational RAG: Enable a chatbot experience over an external source of data
- Agents: Build a chatbot that can take actions

This tutorial will cover the basics which will be helpful for those two more advanced topics.
"""

import logging
import re
from pathlib import Path
from typing import Any, Callable, Dict, Union

from fastapi import HTTPException, Request
from langchain_community.chat_message_histories import FileChatMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.language_models.chat_models import BaseChatModel
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import ConfigurableFieldSpec
from langchain_core.runnables.base import Runnable
from langchain_core.runnables.history import RunnableWithMessageHistory
from typing_extensions import TypedDict


def _is_valid_identifier(value: str) -> bool:
    """Check if the value is a valid identifier."""
    # Use a regular expression to match the allowed characters
    valid_characters = re.compile(r"^[a-zA-Z0-9-_]+$")
    return bool(valid_characters.match(value))


def per_request_config_modifier(
    config: Dict[str, Any], request: Request
) -> Dict[str, Any]:
    """Update the config"""
    config = config.copy()
    configurable = config.get("configurable", {})
    user_id = request.cookies.get("user_id", None)
    if user_id is None:
        raise HTTPException(
            status_code=400,
            detail="No user id found. Please set a cookie named 'user_id'.",
        )
    conversation_id = request.cookies.get("conversation_id", None)
    if user_id is None:
        raise HTTPException(
            status_code=400,
            detail="No conversation id found. Please set a cookie named 'conversation_id'.",
        )

    configurable["user_id"] = user_id
    configurable["conversation_id"] = conversation_id
    config["configurable"] = configurable
    return config


def create_session_factory(
    base_dir: Union[str, Path]
) -> Callable[[str], BaseChatMessageHistory]:
    """Create a factory that can retrieve chat histories.

    the chat histories are keyed by user ID and conversation ID.
    """
    _base_dir = Path(base_dir)
    _base_dir.mkdir(parents=True, exist_ok=True)

    def get_chat_history(user_id: str, conversation_id: str) -> FileChatMessageHistory:
        if not _is_valid_identifier(user_id):
            msg = f"User ID {user_id} is not a valid format. "
            "User ID must only contain alphanumeric characters, hyphens, and underscores."
            "Please include a valid cookie in the request headers called 'user-id'."
            raise ValueError(msg)
        if not _is_valid_identifier(conversation_id):
            msg = f"Conversation ID {conversation_id} is not a valid format. "
            "Conversation ID must only contain alphanumeric characters, hyphens, and underscores."
            "Please include a valid cookie in the request headers called 'conversation-id'."
            raise ValueError(msg)

        user_dir = _base_dir / user_id
        user_dir.mkdir(parents=True, exist_ok=True)
        file_path = user_dir / f"{conversation_id}.json"
        logging.info("get chat history from %s", str(file_path))
        return FileChatMessageHistory(str(file_path))

    return get_chat_history


class InputChat(TypedDict):
    """Input for the chat endpoint."""

    text: str


def get_chain(model: BaseChatModel) -> Runnable:
    """Get translator chain."""
    system_template = (
        "You are a helpful assistant. Answer all questions to the best of your ability."
    )
    prompt_template = ChatPromptTemplate.from_messages(
        [
            ("system", system_template),
            MessagesPlaceholder(variable_name="history"),
            ("human", "{text}"),
        ]
    )
    parser = StrOutputParser()
    chain: Runnable = prompt_template | model | parser
    chain_with_history = RunnableWithMessageHistory(
        chain,
        create_session_factory("chat_histories"),
        input_messages_key="text",
        history_messages_key="history",
        history_factory_config=[
            ConfigurableFieldSpec(
                id="user_id",
                annotation=str,
                name="User ID",
                description="Unique identifier for the user",
                default="",
                is_shared=True,
            ),
            ConfigurableFieldSpec(
                id="conversation_id",
                annotation=str,
                name="Conversation ID",
                description="Unique identifier for the conversation",
                default="",
                is_shared=True,
            ),
        ],
    ).with_types(input_type=InputChat)
    return chain_with_history
