from google.adk import Agent 
from google.adk.tools import google_search
from . import prompt

MODEL = "moodel_name"

trend_analyzer = Agent(
    model=MODEL,
    name="trend_analyser",
    instruction=prompt.TREND_ANALYSER,
    output="trend_analyser",
    tools=[google_search],
    
)
