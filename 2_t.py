from dotenv import load_dotenv
from langchain.agents import AgentType
from langchain.agents.agent_toolkits import create_python_agent
from langchain.chat_models import ChatOpenAI
from langchain.tools import PythonREPLTool
from langchain.schema import BaseOutputParser
import os
from dotenv import load_dotenv
from langchain.agents import AgentType, create_csv_agent, initialize_agent
from langchain.agents.agent_toolkits import create_python_agent
from langchain.chat_models import ChatOpenAI
from langchain.tools import PythonREPLTool, Tool
from langchain.utilities import SerpAPIWrapper
from langchain.agents import AgentType, initialize_agent
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.agents import Tool
from langchain.tools import PythonREPLTool

# Do this so we can see exactly what's going on under the hood
import langchain

langchain.debug = True

load_dotenv()


def main():

    chat_agent_executor = create_python_agent(
        llm=ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo-16k-0613"),
        tool=PythonREPLTool(),
        agent_type=AgentType.OPENAI_FUNCTIONS,
        verbose=True,
    )

    python_agent_executor = create_python_agent(
        llm=ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo"),
        tool=PythonREPLTool(),
        agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
    )
    #
    # python_agent_executor.run(
    #     """
    #     Please develop a webpage that allows me to move a box with my mouse.
    #     The box should be 100px by 100px and should be red.
    #     The ports you can use are 4500 and 7000.
    #     you should use the python library flask.
    #     you should run the server with the command python app.py.
    #     you must return "localhost:4500" as the url where the webpage is hosted.
    # """
    # )

    grand_agent = initialize_agent(
        tools=[
            Tool(
                name="PythonAgent",
                func=python_agent_executor.run,
                description="""
                           useful when you need to transform natural language and write from it python
                           and execute the python code,
                           returning the results of the code execution,
                               """,
            ),
            Tool(
                name="ChatAgent",
                func=chat_agent_executor.run,
                description="""
                            useful when you need to transform natural language and write from it python
                            and execute the python code,
                            returning the results of the code execution,
                                """,
            ),
        ],
        llm=ChatOpenAI(temperature=0, model="gpt-3.5-turbo"),
        agent_type=AgentType.OPENAI_FUNCTIONS,
        verbose=True,
    )

    grand_agent.run(
        """
        Please develop a webpage that allows me to move a box with my mouse.
        The box should be 100px by 100px and should be red.
        The ports you can use are 4500 and 7000.
    """
    )


if __name__ == "__main__":
    main()
