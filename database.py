import sqlite3
import json


def create_db():
    conn = sqlite3.connect('website_sentiment.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS sentiment_results
        (id INTEGER PRIMARY KEY AUTOINCREMENT, 
         url TEXT NOT NULL UNIQUE,
         scores TEXT NOT NULL,
         data TEXT NOT NULL)
    ''') # for data have to json load and json dump
    conn.commit()
    conn.close()


def add_sentiment_for_url(url, scores, data):
    conn = sqlite3.connect('website_sentiment.db')
    c = conn.cursor()
    try:
        c.execute("INSERT INTO sentiment_results (url, scores, data) VALUES (?, ?, ?)", (url, json.dumps(scores), json.dumps(data)))
        conn.commit()
    except sqlite3.IntegrityError:
        # URL already exists
        pass
    finally:
        conn.close()

def get_sentiment_for_url(url):
    """
    Retrieves sentiment results for a given URL, including deserializing
    the JSON 'data' column back into a Python list of dictionaries.
    """
    conn = sqlite3.connect('website_sentiment.db')
    c = conn.cursor()

    # 1. SELECT the 'data' column along with the others
    c.execute("""
        SELECT scores, data 
        FROM sentiment_results 
        WHERE url = ?
    """, (url,))
    
    result = c.fetchone()
    conn.close()

    if result:
        # result is a tuple: (bias, political_leaning, attitude, json_string_data)
        json_string_scores, json_string_data = result
        
        # 2. Deserialize the JSON string back into a Python list/dict
        try:
            data_list = json.loads(json_string_data)
            scores_list = json.loads(json_string_scores)
        except json.JSONDecodeError:
            print(f"Error decoding JSON data for URL: {url}")
            data_list = None # Handle potential decoding errors gracefully
            scores_list = None
        
        # 3. Return all values, with the deserialized data
        return {
            'scores': scores_list,
            'data': data_list  # This is now a Python list of dictionaries
        }
if __name__ == '__main__':
    create_db()
