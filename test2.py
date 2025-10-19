from article_analysis import analyse_article
import json

print(analyse_article('https://www.bbc.co.uk/news/articles/cn97gjqgq9po'))

"""
title: ...
mainterxt:...
summary:...
related_articles: [
    {
    title:..
    snippet:...
    url:...
    },
    ...
 

]

data['related_articles'][0]['title']

"""
