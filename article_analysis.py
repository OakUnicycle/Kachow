from newsplease import NewsPlease
import openai_integration as ai
import json


def analyse_article(url):
    data = {}

    article = NewsPlease.from_url('https://www.bbc.co.uk/news/articles/c93dqew8l3xo')

    data['title'] = article.title
    data['maintext'] = article.maintext

    related_articles = ai.get_related_articles_and_summary(article.maintext)

    data['summary'] = related_articles['summary']
    data['related_articles'] = related_articles['results']

    return data
