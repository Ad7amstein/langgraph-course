from typing import TypedDict, NotRequired, Optional
from langgraph.graph import StateGraph, START, END


class state(TypedDict):
    input : str
    # output : NotRequired[str]
    output : Optional[str]
    steps : int

# def process(state: state) -> state:
#     print(f"State keys: {state.keys()}")
#     return {
#         "input": state["input"],
#         "output": state["input"].upper(),
#         "steps": state["steps"]+1
#     }

def build_graph():

    def process(state: state) -> state:
        print(f"State keys: {state.keys()}")
        return {
            "input": state["input"],
            "output": state["input"].upper(),
            "steps": state["steps"]+1
        }
    graph = StateGraph(state) 

    # Add Nodes
    graph.add_node("process", process)

    #Add Edges
    graph.add_edge(START, "process")
    graph.add_edge("process", END)


    return graph.compile()

build_graph.x = 5
    
def main():
    # app = build_graph()
    # result = app.invoke({"input": "Adham & Tharwat", "steps": 0})
    # print("Graph Results: \n")
    # print(result)
    print(build_graph.x)


if __name__ == "__main__":
    main()
