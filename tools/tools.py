from langchain.utilities import SerpAPIWrapper


def serp_search(name: str):
    """
    serp search
    """
    serpapi = SerpAPIWrapper()
    result = serpapi.run(f"{name}")
    print("result: ", result)
    return result
