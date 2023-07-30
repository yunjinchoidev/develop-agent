from dotenv import load_dotenv
from langchain.agents import AgentType
from langchain.agents.agent_toolkits import create_python_agent
from langchain.chat_models import ChatOpenAI
from langchain.tools import PythonREPLTool

load_dotenv()


def main():

    python_agent_executor = create_python_agent(
        llm=ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo"),
        tool=PythonREPLTool(),
        agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
    )

    python_agent_executor.run(
        """
        Please develop a webpage that displays "hello world!" just string.
        you can use fastapi.fastapi is already installed.
        you can use uvicorn. uvicorn is already installed.
        you dont have to install anything.
        source code saved in app.py
        note that you can look syntax of fastapi in the documentation.
        The ports you can use are 4500 port.
        the command is uvicorn app:app --port 4500
        you should run it in the terminal of the server
        you can use the terminal in the server.
        you should present me "localhost:4500" so that I can see the result.
    """
    )


if __name__ == "__main__":
    main()
