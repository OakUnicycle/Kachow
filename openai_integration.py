import os
import json
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()  # loads .env file
API_KEY = os.getenv("OPENAI_API_KEY")


# Set your API key
os.environ["OPENAI_API_KEY"] = API_KEY
client = OpenAI()

# A prompt designed to extract key info and create search queries
# We use JSON mode for a reliable, parsable output
system_prompt_queries = """
You are a news analyst. Your task is to analyze the provided article
and generate 3-5 relevant search queries to find similar, more recent
news articles.

Return your answer in JSON format with two keys:
1. "main_topic": A brief summary of the main event.
2. "search_queries": A list of 5 search strings.
"""

def generate_analysis(source_article_text):
    try:
        response = client.chat.completions.create(
            model="gpt-5-nano",  # Use a modern, capable model
            response_format={"type": "json_object"},
            messages=[
                {"role": "system", "content": system_prompt_queries},
                {"role": "user", "content": source_article_text}
            ]
        )

        # Parse the JSON response
        analysis = json.loads(response.choices[0].message.content)

        print(f"Main Topic: {analysis['main_topic']}\n")
        print("Generated Search Queries:")
        for query in analysis['search_queries']:
            print(f"  - {query}")

        return analysis

    except Exception as e:
        print(f"An error occurred: {e}")

system_prompt_verify = """
You are an AI assistant. Your task is to check a list of search results
against a base article summary. You must exclude any result that is
clearly unrelated (e.g., a different topic, a login page, a generic biography).

The user will provide a `BASE_ARTICLE_SUMMARY` and a `SEARCH_RESULTS` list.

Respond **only** with a JSON object. This object must have one key,
`filtered_results`, which is a list. Each item in the list must be an
object containing the original `index`, `title`, a boolean `is_related`
(`true` or `false`), and a brief `reasoning` for your decision.
"""

def verify_related(summary, results):
    """
    Output: json:
    {
        index,
        title,
        is_related,
        reasoning
    }
    """
    data = [{'index': index, 'title': i['title'], 'snippet': i['snippet'], 'url': i['link']} for (index, i) in enumerate(results)]

    user_prompt = f"""
    Please filter these search results.

    BASE_ARTICLE_SUMMARY:
    {summary}

    SEARCH_RESULTS:
    {json.dumps(data, indent=2)}
    """

    try:
        response = client.chat.completions.create(
            model="gpt-5-nano",  # Use a modern, capable model
            response_format={"type": "json_object"},
            messages=[
                {"role": "system", "content": system_prompt_verify},
                {"role": "user", "content": user_prompt}
            ]
        )

        # Parse the JSON response
        analysis = json.loads(response.choices[0].message.content)

        print(response.choices[0].message.content)

    except Exception as e:
        print(f"An error occurred: {e}")
