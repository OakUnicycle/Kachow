
from flask import Flask, render_template, request
import sqlite3
import validators
from article_analysis import analyse_article
import json
from database import get_sentiment_for_url, add_sentiment_for_url
from wv_scoring import getting_scores
app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def index():
    url = request.form.get('url')
    if not url or validators.url(url) != True:
        return render_template('index.html', scores={}, related_articles=[], is_initial_load=True)

    db_result = get_sentiment_for_url(url)
    if db_result == None: # if not in database -> find info
        data = analyse_article(url)
        scores = getting_scores(url)
        add_sentiment_for_url(url, scores, data)
    else:
        data = db_result['data']
        scores = db_result['scores']
    
    return render_template('index.html', title = data['title'], source = data['source_domain'], main_text = data['summary'], related_articles = data['related_articles'], scores=scores, is_initial_load=False)

if __name__ == '__main__':
    app.run(debug=True)
