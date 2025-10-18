import os
from googleapiclient.discovery import build
import json
from dotenv import load_dotenv

load_dotenv()  # loads .env file
API_KEY = os.getenv("GOOGLE_CLOUD_API_KEY")
CSE_ID = os.getenv("CSE_ID")

def google_search(query, num_results=10):
    """
    Performs a Google Custom Search.
    
    Args:
        query (str): The search query.
        api_key (str): Your Google API Key.
        cse_id (str): Your Custom Search Engine ID.
        num_results (int): Number of results to return (max 10 per call).

    Returns:
        list: A list of search result items, or None if an error occurs.
    """
    try:
        # Build the service object
        service = build("customsearch", "v1", developerKey=API_KEY)
        
        # Make the API call
        res = service.cse().list(
            q=query,       # The search query
            cx=CSE_ID,     # The Custom Search Engine ID
            num=num_results  # Number of results to retrieve
        ).execute()
        
        # Return the list of 'items' (search results)
        result = [{'title': i['title'], 'snippet': i['snippet'], 'link': i['link']} for i in res.get('items', [])]
        return result

    except Exception as e:
        print(f"An error occurred: {e}")
        # This can happen if your quota is exceeded or keys are wrong
        return None

def print_results(results):

    if results:
        print(f"--- Found {len(results)} results")
        
        # Loop through and print the results
        for i, result in enumerate(results):
            print(f"\nResult {i+1}:")
            print(f"  Title: {result['title']}")
            print(f"  Snippet: {result['snippet']}")
            print(f"  URL: {result['link']}")
    else:
        print("No results found or an error occurred.")
