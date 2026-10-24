# Basics

## Notes

### Langgraph vs. Langchain

Simple workflow (e.g. simple chatbot) => use langchain
Complex workflow => use langgraph

Langchain => Components
Langgraph => Workflow

### Document retrieval workflow:

Grade docs (grade the retrieved docs)
Rewrite query (rewrite the query if the docs is not relevant)


State has everything and each node receives the whole state, but you control what the agent/llm receives


- `NotRequired`: The key can be omitted.
- `Optional`: The value can be `None`, but the key is still required.

## Code Planning

Imports

State:
- input
- output
- steps

Process:
- step+1
- Capitalize the input, and put int the output

Build graph function:
- Start -> process -> End

Invoke in main function
