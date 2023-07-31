from dotenv import load_dotenv
from langchain.agents import AgentType
from langchain.agents.agent_toolkits import create_python_agent
from langchain.chat_models import ChatOpenAI
from langchain.tools import PythonREPLTool
from langchain.schema import BaseOutputParser
import os

load_dotenv()


def main():

    python_agent_executor = create_python_agent(
        llm=ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo-16k-0613"),
        tool=PythonREPLTool(),
        agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
    )

    python_agent_executor.run(
        """
        Please develop a webpage that allows me to move a box with my mouse.        
        The ports you can use are 4500 and 7000.
        you should run it on localhost.
    """
    )


if __name__ == "__main__":
    main()
