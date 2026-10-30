from langgraph.graph import StateGraph, START, END, add_messages, MessagesState
from typing import TypedDict, List , Annotated , Dict 
from langchain.messages import HumanMessage, AIMessage


class GraphState(MessagesState):
    score: int
    essay: str


def grade_node (state: GraphState)  -> Dict:
    return {"score": 70, "messages": [AIMessage(content="your score is 70")]}

def feedback_node(state: GraphState) -> Dict:
    return {"messages": [AIMessage(content="too low, please study more.")]}

def aggregate_node(state: GraphState) -> Dict:
    return state

def pass_node (state:GraphState) -> Dict:
    return{"messages": [AIMessage(content="you passed!")]}

def fail_node (state:GraphState) -> Dict:
    return{"messages": [AIMessage(content="you failed :)")]}

def pass_or_fail(state: GraphState) -> str:
    if state["score"] >= 75:
        return "pass"
    else:
        return "fail"

graph = StateGraph(GraphState)

graph.add_node("feed_back", feedback_node)
graph.add_node("grade", grade_node)
graph.add_node("pass_node", pass_node)
graph.add_node("fail_node", fail_node)
graph.add_node("aggregate", aggregate_node)

graph.add_edge(START, "grade")
graph.add_edge(START, "feed_back")
graph.add_conditional_edges(
    "aggregate",
    pass_or_fail,
    {
        "pass": "pass_node",
        "fail": "fail_node"
    }
)

graph.add_edge(["pass_node","fail_node"], END)

app = graph.compile()

initial = {"essay":"allaylo  walalkayl"}
result = app.invoke(initial)

print(result)