
from flask import Flask, render_template, request
import sqlite3
import validators
from bias_checker import bias_checker
from article_analysis import analyse_article

app = Flask(__name__)

def get_sentiment_for_url(url):
    conn = sqlite3.connect('website_sentiment.db')
    c = conn.cursor()
    c.execute("SELECT bias, political_leaning, attitude FROM sentiment_results WHERE url = ?", (url,))
    result = c.fetchone()
    conn.close()
    if result:
        return result
    return None

def add_sentiment_for_url(url, bias, political_leaning, attitude):
    conn = sqlite3.connect('website_sentiment.db')
    c = conn.cursor()
    try:
        c.execute("INSERT INTO sentiment_results (url, bias, political_leaning, attitude) VALUES (?, ?, ?, ?)", (url, bias, political_leaning, attitude))
        conn.commit()
    except sqlite3.IntegrityError:
        # URL already exists
        pass
    finally:
        conn.close()

@app.route('/', methods=['POST','GET'])
def index():
    url = request.form.get('url')
    print(validators.url(str(url)))
    if validators.url(url) != True:
        return render_template('index.html', url = 'Not a  url')
    if get_sentiment_for_url(url) == None:
        results = bias_checker(url)
        add_sentiment_for_url(url, results[0], results[1], results[2])
    else:
        pass

    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
