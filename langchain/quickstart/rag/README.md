# Retrieval Augmented Generation (RAG)

If you want to build AI applications that can reason about private data or data introduced after a model's cutoff date,
you need to augment the knowledge of the model with the specific information it needs.
The process of bringing the appropriate information and inserting it into the model prompt is known as Retrieval Augmented Generation (RAG).

## Prerequisites
Setup API keys and python env. (See [README.md](../README.md))

## Concepts
### Indexing
a pipeline for ingesting data from a source and indexing it. This usually happens offline.

1. Load
2. Split
3. Store

### Retrieval and generation
The actual RAG chain, which takes the user query at run time and retrieves the relevant data from the index, then passes that to the model.


## References
- https://python.langchain.com/v0.2/docs/tutorials/rag/
