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

    python_agent_executor.run("""
        Please develop a webpage that allows me to move a box with my mouse.
        the html file should save in static folder index.html.        
        watch out triple-quoted string literal.
        and mapping by fastapi. 
        fastapi is already installed in this project.
        you can use uvicorn. uvicorn is already installed.
        you dont have to install anything.
        you should use HTMLResponse to serve your html file and save fastapi file in app.py.
        you should save file.
        you should use port 4500.
        you can use the terminal in the server.
        you should present me result "localhost:4500" so that I can see the result.
    """)

if __name__ == "__main__":
    main()