
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
    if validators.url(url) != True: # checks if text is a url
        return render_template('index.html', url = 'Not a  url')
    
    if get_sentiment_for_url(url) == None: # if not in database -> find info
        data = analyse_article(url)
        scores = getting_scores(url)
        add_sentiment_for_url(url, scores, data)
    else:
        data = get_sentiment_for_url(url)['data']
    data['authors'] = 'tolkien'
    
    return render_template('index.html', title = data['title'], author = data['authors'], main_text = data['maintext'], results = data['related_articles'])

if __name__ == '__main__':
    app.run(debug=True)
