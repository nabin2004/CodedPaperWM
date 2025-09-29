import requests
import xml.etree.ElementTree as ET

def fetch_arxiv_papers(query, max_results=10):
    """
    Fetch papers from arXiv for a given query.
    Returns a list of dicts with title, authors, published, summary, and link.
    """
    # URL encode spaces for the query
    query = query.replace(" ", "+")
    url = f'http://export.arxiv.org/api/query?search_query=all:{query}&start=0&max_results={max_results}'
    
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"API request failed with status {response.status_code}")
    
    root = ET.fromstring(response.content)
    ns = {'atom': 'http://www.w3.org/2005/Atom'}
    
    papers = []
    for entry in root.findall('atom:entry', ns):
        papers.append({
            'title': entry.find('atom:title', ns).text.strip(),
            'summary': entry.find('atom:summary', ns).text.strip(),
            'authors': [a.find('atom:name', ns).text for a in entry.findall('atom:author', ns)],
            'published': entry.find('atom:published', ns).text,
            'link': entry.find('atom:id', ns).text
        })
    return papers


def filter_recent(papers, year=2022):
    return [p for p in papers if int(p['published'][:4]) >= year]


def summarize_papers(papers, summarizer_func):
    for p in papers:
        p['summary'] = summarizer_func(p['summary'])
    return papers

if __name__ == "__main__":
    query = "embodied AI"
    papers = fetch_arxiv_papers(query, max_results=5)
    recent_papers = filter_recent(papers, year=2022)
    
    for p in recent_papers:
        print("Title:", p['title'])
        print("Authors:", ", ".join(p['authors']))
        print("Published:", p['published'])
        print("Summary:", p['summary'])
        print("Link:", p['link'])
        print("-" * 80)