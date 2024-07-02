# Retrieval Augmented Generation (RAG)

If you want to build AI applications that can reason about private data or data introduced after a model's cutoff date,
you need to augment the knowledge of the model with the specific information it needs.
The process of bringing the appropriate information and inserting it into the model prompt is known as Retrieval Augmented Generation (RAG).

## Prerequisites
Setup API keys and python env. (See [README.md](../README.md))

## Concepts
### Indexing
a pipeline for ingesting data from a source and indexing it. This usually happens offline.

![image](https://github.com/Curt-Park/TIL/assets/14961526/dffd838f-3c01-42d3-89ea-19edf276cd8d)

1. Load: Data load that is done with [Document Loaders](https://python.langchain.com/v0.2/docs/concepts/#document-loaders)
2. Split: Splits documents into smaller chunks by [Text Splitters](https://python.langchain.com/v0.2/docs/concepts/#text-splitters)
3. Store: the chunks are stored, so that they can later be searched over. It's done using [VectorStore](https://python.langchain.com/v0.2/docs/concepts/#vector-stores) and [Embeddings](https://python.langchain.com/v0.2/docs/concepts/#embedding-models)

### Retrieval and generation
The actual RAG chain, which takes the user query at run time and retrieves the relevant data from the index, then passes that to the model.

![image](https://github.com/Curt-Park/TIL/assets/14961526/662692d5-d54b-4433-a63a-11c6eb3340f1)

1. Retrieve: Given a user input, relevant splits are retrieved from storage using a [Retriever](https://python.langchain.com/v0.2/docs/concepts/#retrievers).
2. Generate: A [ChatModel](https://python.langchain.com/v0.2/docs/concepts/#chat-models) / [LLM](https://python.langchain.com/v0.2/docs/concepts/#llms) produces an answer using a prompt that includes the question and the retrieved data


## References
- https://python.langchain.com/v0.2/docs/tutorials/rag/
