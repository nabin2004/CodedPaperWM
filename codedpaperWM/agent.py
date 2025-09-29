from google.adk.agents import LlmAgent
from google.adk.tools.agent_tool import AgentTool

from . import prompt

# Other agents
from .sub_agents.academic_newresearch import academic_newresearch_agent
from .sub_agents.academic_websearch import academic_websearch_agent

MODEL = "GEMMA3-270m"

codedpaperWM = LlmAgent(
    name="codedpaperWM",
    model=MODEL,
    description=(
        "Nanannanananan nananana nananan"
    ),
    instruction=prompt.ACADEMIC_COORDINATOR_PROMPT,
    output_key="seminal_paper",
    tools=[
        AgentTool(agent=academic_websearch_agent),
        AgentTool(agent=academic_newresearch_agent),
    ]
)

root_agent = academic_coordinator