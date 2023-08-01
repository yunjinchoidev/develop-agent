from dotenv import load_dotenv
from langchain.agents import AgentType
from langchain.agents.agent_toolkits import create_python_agent
from langchain.chat_models import ChatOpenAI
from langchain.tools import PythonREPLTool
from langchain.utilities import SerpAPIWrapper
from langchain.agents import AgentType, initialize_agent
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.agents import Tool
from langchain.tools import PythonREPLTool

# Do this so we can see exactly what's going on under the hood
import langchain

# langchain.debug = True


load_dotenv()


def main():

    python_agent_executor = create_python_agent(
        llm=ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo"),
        tool=PythonREPLTool(),
        agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
    )

    # python_agent_executor.run(
    #     """
    #         develop a add, delete cotrol todo webpage.
    #         the working file should save in static folder index.html.
    #         and mapping by fastapi.
    #         fastapi is already installed in this project.
    #         you can use uvicorn. uvicorn is already installed.
    #         you don't have to install anything.
    #         you should use HTMLResponse to serve your html file and save fastapi file in app.py.
    #         you should save file.
    #         you should present me result "localhost:4500" so that I can see the result.
    #
    # """
    # )
    # python_agent_executor.run(
    #     """
    #         develop a add, delete cotrol todo webpage.
    #         the working file should save in static folder index.html.
    #         and mapping by fastapi.
    #         fastapi is already installed in this project.
    #         you can use uvicorn. uvicorn is already installed.
    #         you don't have to install anything.
    #         you should use HTMLResponse to serve your html file and save fastapi file in app.py.
    #         you should save file.
    #         you should present me result "localhost:4500" so that I can see the result.
    #
    # """
    # )

    python_agent_executor.run(
        """
            Develop a add, delete control todo webpage.
            neumorphism style is recommended.
            Save the HTML file in a static folder named 'index.html'.
            Pay attention to triple-quoted string literals.
            Map it using FastAPI.
            There is no need to install anything.
            Use HTMLResponse to serve your HTML file.
            Save the FastAPI file as 'app.py'.
            The available ports you can use are 4500 and 7000.
            Use uvicorn to launch the FastAPI server, making it directly accessible.    
    """
    )


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
            description="""            
                Useful when you need to answer questions about current events. 
                You should ask targeted questions.
            """,
        ),
        Tool(
            name="python_repl",
            func=PythonREPLTool(),
            description="python_repl, useful for when you need to run python code, and get the output, or save the output to a file",
        ),
    ]

    mrkl = initialize_agent(
        tools=tools, llm=llm, agent=AgentType.OPENAI_MULTI_FUNCTIONS, verbose=True
    )

    run = mrkl.run(name)

    with open("result.txt", "w") as f:
        f.write(run)

    return run


if __name__ == "__main__":

    x = find_code_search_by_serp(
        "Neumorphism style Todo web page that can add, delete, control todo list. The ports you can use are 4500 and 7000."
    )

    python_agent_executor = create_python_agent(
        llm=ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo"),
        tool=PythonREPLTool(),
        agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
    )

    python_agent_executor.run(
        """
        I provide a todo web page that can add, delete, control todo list.
        Follow this and Develope
        The ports you can use are 4500 and 7000.
        You Should Run Server.
        : 
        """
        + x
    )

    # main()
