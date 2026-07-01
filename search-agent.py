from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from tavily import TavilyClient

load_dotenv()

llm = ChatOpenAI(model_name="gpt-4o", temperature=0)
tavily_client = TavilyClient()

@tool
def search(query:str)->str:
    """
    Tool that searches over internet

    Args:
        query (str): The search query
    Returns:
        str: The search results
    """
    print(f"Searching for: {query}")
    return tavily_client.search(query=query)

tools=[search]
agent = create_agent(model=llm, tools=tools)

def main():
    agent_response = agent.invoke({
        "messages": HumanMessage(content="What is the weather in Tokyo today?")
    })
    print(agent_response)


if __name__ == "__main__":
    main()