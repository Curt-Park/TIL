"""Building an embeddings index.

Reference:
    https://platform.openai.com/docs/tutorials/web-qa-embeddings
"""

import argparse
import os
from typing import Callable

import numpy as np
import pandas as pd
import tiktoken
from tiktoken.core import Encoding

from openai import OpenAI


def embedding_function(s: str, client: OpenAI, model: str = "text-embedding-ada-002") -> list[float]:
    embedding = client.embeddings.create(input=s, model=model).data[0].embedding
    return embedding


def split_into_many(text: str, tokenizer: Encoding, max_tokens: int = 500) -> list[str]:
    """Function to split the text into chunks of a maximum number of tokens."""
    # Split the text into sentences
    sentences = text.split(". ")

    # Get the number of tokens for each sentence
    n_tokens = [len(tokenizer.encode(" " + sentence)) for sentence in sentences]

    chunks, chunk = [], []
    tokens_so_far = 0
    # Loop through the sentences and tokens joined together in a tuple
    for sentence, token in zip(sentences, n_tokens):
        # If the number of tokens so far plus the number of tokens in the current sentence is greater
        # than the max number of tokens, then add the chunk to the list of chunks and reset
        # the chunk and tokens so far
        if tokens_so_far + token > max_tokens:
            chunks.append(". ".join(chunk) + ".")
            tokens_so_far = 0
            chunk = []

        # If the number of tokens in the current sentence is greater than the max number of
        # tokens, go to the next sentence
        if token > max_tokens:
            continue

        # Otherwise, add the sentence to the chunk and add the number of tokens to the total
        chunk.append(sentence)
        tokens_so_far += token + 1

    return chunks


def get_dataframe_from_files(
    text_dir: str,
    tokenizer: Encoding,
    max_tokens: int,
    embedding_function: Callable[[str], np.ndarray],
) -> pd.DataFrame:
    """Get all the text files in the text directory."""
    texts: list[str] = []
    for filename in os.listdir(text_dir):
        # Open the file and read the text.
        with open(os.path.join(text_dir, filename), "r", encoding="UTF-8") as f:
            text = f.read()
        text = " ".join(text.split())

        # If the number of tokens is greater than the max number of tokens, split the text into chunks
        texts += split_into_many(text, tokenizer, max_tokens)

    df = pd.DataFrame(texts, columns=["text"])
    df["embeddings"] = df.text.apply(embedding_function)
    df["n_tokens"] = df.text.apply(lambda x: len(tokenizer.encode(x)))
    return df


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--text-dir", type=str, required=True)
    parser.add_argument("--max-tokens", type=int, default=500)
    parser.add_argument("--tokenizer", type=str, default="cl100k_base")
    args = parser.parse_args()

    tokenizer = tiktoken.get_encoding(args.tokenizer)
    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
    df = get_dataframe_from_files(
        args.text_dir,
        tokenizer,
        args.max_tokens,
        lambda s: embedding_function(s, client),
    )

    local_domain = os.path.split(args.text_dir)[-1]
    os.makedirs("embeddings", exist_ok=True)
    df.to_csv(os.path.join("embeddings", f"{local_domain}.csv"))
