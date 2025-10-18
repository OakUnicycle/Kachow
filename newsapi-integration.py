import requests
import os
from dotenv import load_dotenv

load_dotenv()  # loads .env file
API_KEY = os.getenv("NEWSAPI_KEY")

# Replace with your actual NewsAPI key
URL = "https://newsapi.org/v2/top-headlines"

params = {
    "country": "us",       # or another country code
    "pageSize": 5,         # number of articles
    "apiKey": API_KEY
}

response = requests.get(URL, params=params)

if response.status_code == 200:
    data = response.json()
    for article in data["articles"]:
        print(f"Title: {article['title']}")
        print(f"Source: {article['source']['name']}")
        print(f"URL: {article['url']}")
        print("-" * 80)
else:
    print(f"Error: {response.status_code}")
    print(response.text)
