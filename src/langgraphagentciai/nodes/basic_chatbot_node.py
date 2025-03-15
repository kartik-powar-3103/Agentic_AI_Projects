from src.langgraphagentciai.state.state import State

class BasicChatbotNode:
    def __init__(self, model):
        """
        Basic chatbot logic implementation.
        """
        self.llm = model 
    
    def process(self, state: State) -> dict:
        return {"messages": self.llm.invoke(state["messages"])}
    