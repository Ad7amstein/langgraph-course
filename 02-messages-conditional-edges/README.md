# reducers, messages, and conditional edges

## Flow

start
- grade essay
- feedback message

conditional edge

- pass
- fail

## Code structure

imports

state

nodes

graph

# Notes

Reducers: determine how the values in the state should be updated

Take a closer look at `Annotated`
Is the return from any node the state only?

`add_messages` reducer: appends messages to the list of messages

Try updating the same key at the same time

