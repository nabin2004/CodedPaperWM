# classifier agent 
from google.adk import Agent 
from google.adk.tools import google_search

MODEL = "model_here"

classifier_agent = Agent(
    model= MODEL,
    name="paper-classifier",
    instruction=prompt.ACADEMIC_PAPER_CLASSIFIER,
    output_key="recent_paper_classification",
    tools=[google_search],
)
