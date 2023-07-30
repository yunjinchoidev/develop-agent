from langchain.utilities import SerpAPIWrapper
from langchain.agents import AgentType, initialize_agent
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.agents import Tool

# Do this so we can see exactly what's going on under the hood
import langchain

langchain.debug = True

load_dotenv()


def serp_search(name: str):
    """
    serp search
    """
    serpapi = SerpAPIWrapper()
    result = serpapi.run(f"{name}")
    print("result: ", result)
    return result


def find_code_search_by_serp(name: str):
    # Initialize the OpenAI language model
    # Replace <your_api_key> in openai_api_key="<your_api_key>" with your actual OpenAI key.
    llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo-0613")

    # Initialize the SerpAPIWrapper for search functionality
    # Replace <your_api_key> in openai_api_key="<your_api_key>" with your actual SerpAPI key.
    search = SerpAPIWrapper()

    # Define a list of tools offered by the agent
    tools = [
        Tool(
            name="Search",
            func=search.run,
            description="Useful when you need to answer questions about current events. You should ask targeted questions.",
        )
    ]
    mrkl = initialize_agent(
        tools, llm, agent=AgentType.OPENAI_MULTI_FUNCTIONS, verbose=True
    )

    return mrkl.run(name)


if __name__ == "__main__":

    print(find_code_search_by_serp("Tetris Python Code"))
