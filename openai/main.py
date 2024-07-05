import argparse
import logging
import os
from typing import Any

import pandas as pd
from scipy.spatial.distance import cosine

from embed_text import embedding_function
from openai import OpenAI

logger = logging.getLogger(__name__)
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))


def create_context(question: str, df: pd.DataFrame, max_len: int = 1800) -> str:
    """Create a context for a question by finding the most similar context from the dataframe."""
    # Get the embeddings for the question
    q_embeddings = embedding_function(question, client)

    # Get the distances from the embeddings
    df["distances"] = df["embeddings"].apply(lambda x: cosine(q_embeddings, x))

    returns = []
    cur_len = 0
    # Sort by distance and add the text to the context until the context is too long
    for i, row in df.sort_values("distances", ascending=True).iterrows():
        # Add the length of the text to the current length.
        cur_len += row["n_tokens"] + 4
        # If the context is too long, break
        if cur_len > max_len:
            break
        # Else add it to the text that is being returned
        returns.append(row["text"])

    # Return the context
    return "\n\n###\n\n".join(returns)


def answer_question(
    df: pd.DataFrame,
    question: str,
    max_context_len: int = 1800,
    **kwargs: Any,
) -> str:
    """Answer a question based on the most similar context from the dataframe texts."""
    context = create_context(question, df, max_len=max_context_len)
    logger.debug("Context:\n" + context)

    messages = [
        {
            "role": "system",
            "content": "Answer the question based on the context below, and if the question can't be answered based on the context, say \"I don't know\"\n\n",
        },
        {
            "role": "user",
            "content": f"Context: {context}\n\n---\n\nQuestion: {question}\nAnswer:",
        },
    ]

    try:
        # Create a chat completion using the question and context
        response = client.chat.completions.create(messages=messages, **kwargs)
        return response.choices[0].message.content
    except Exception as e:
        logger.error(e)
        return ""


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--embeddings", type=str, required=True)
    parser.add_argument("--model", type=str, default="gpt-3.5-turbo")
    args = parser.parse_args()

    # Read embeddings.
    df = pd.read_csv(args.embeddings, index_col=0)
    # String to float.
    df["embeddings"] = df["embeddings"].apply(lambda s: [float(x.strip(" []")) for x in s.split(",")])

    while True:
        print("Question?:")
        question = input()

        # Load the cl100k_base tokenizer which is designed to work with the ada-002 model
        response = answer_question(
            df=df,
            question=question,
            # client.chat.completion.create args.
            model=args.model,
            temperature=0,
            max_tokens=150,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            stop=None,
        )
        print("\nAnswer:\n", response)
        print()
