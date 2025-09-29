from google.adk.tools.agent_tool import AgentTool
from .arxiv_req import fetch_arxiv_papers

class ArxivAgentTool(AgentTool):
    """
    AgentTool wrapper to fetch arXiv papers dynamically.
    """
    def __init__(self):
        # super().__init__(name="arxiv_fetcher", description="Fetch recent papers from arXiv based on a query.")
        pass

    def execute(self, query: str):
        """
        query: string to search for in arXiv
        Returns a list of papers.
        """
        papers = fetch_arxiv_papers(query, max_results=5)
        formatted = []  
        for p in papers:
            formatted.append(
                f"Title: {p['title']}\n"
                f"Authors: {', '.join(p['authors'])}\n"
                f"Published: {p['published']}\n"
                f"Summary: {p['summary']}\n"
                f"Link: {p['link']}\n"
                "------"
            )
        return "\n".join(formatted)
