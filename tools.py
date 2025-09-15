import logging
from livekit.agents import function_tool, RunContext
import requests
from langchain_community.tools import DuckDuckGoSearchRun

@function_tool
async def get_weather(context: RunContext, city: str) -> str:
    """
    Get the current weather for a given city.
    """
    try:
        response = requests.get(f"http://wttr.in/{city}?format=3")
        if response.status_code == 200:
            weather = response.text.strip()  # call strip()!
            logging.info(f"Weather in {city}: {weather}")
            return weather
        else:
            logging.error(f"Failed to get weather for {city}: {response.status_code}")
            return f"Could not retrieve weather for {city}."
    except Exception as e:
        logging.error(f"Error getting weather for {city}: {e}")
        return f"Error retrieving weather for {city}."

@function_tool()
async def search_web(   
                context: RunContext,
                query: str) -> str:
                """
                Perform a web search using DuckDuckGo.
                """
                try:
                        results = DuckDuckGoSearchRun().run(tool_input=query)
                        logging.info(f"Web search results for '{query}': {results}")
                        return results
                except Exception as e:
                        logging.error(f"Error performing web search for '{query}': {e}")
                        return f"Error performing web search for '{query}'."    