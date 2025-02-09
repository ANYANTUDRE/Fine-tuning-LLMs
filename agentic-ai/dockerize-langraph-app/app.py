from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from langchain_community.tools.tavily_search import TavilySearchResults
import os
from langgraph.prebuilt import create_react_agent
from langchain_groq import ChatGroq
import uvicorn


groq_api_key = os.getenv("GROQ_API_KEY", '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')
os.environ["TAVILY_API_KEY"] = os.getenv("TAVILY_API_KEY", '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')

MODEL_NAMES = [
    "llama3-70b-8192",
    "mixtral-8x7b-32768"
]

tool_tavily = TavilySearchResults(max_results=2)
tools = [tool_tavily, ]

app = FastAPI(title='LangGraph AI Agent')


class RequestState(BaseModel):
    system_prompt: str
    model_name: str
    messages: List[str]


@app.post("/chat")
def chat_endpoint(request: RequestState):
    """
    API endpoint to interact with the chatbot using LangGraph and tools.
    Dynamically selects the model specified in the request.
    """
    if request.model_name not in MODEL_NAMES:
        return {"error": "Invalid model name. Please select a valid model."}

    llm = ChatGroq(
        groq_api_key=groq_api_key, 
        model_name=request.model_name
    )
    agent = create_react_agent(
        llm, 
        tools=tools, 
        state_modifier=request.system_prompt
    )

    state = {"messages": request.messages}
    result = agent.invoke(state)

    return result


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)