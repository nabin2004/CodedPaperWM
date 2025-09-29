from codedpaperWM.sub_agents.SummarizerAgent.agent import summarizer_agent

query = "embodied AI"

# Use the agent
result = summarizer_agent(query)

# Print the output
print("=== Summarizer Output ===")
print(result)
