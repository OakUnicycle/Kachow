from newsplease import NewsPlease
import openai_integration as ai
import json


article = NewsPlease.from_url('https://www.bbc.co.uk/news/articles/c93dqew8l3xo')
print("TITLE:")
print(article.title)


print("\n\n\n")
print("Finding Related articles\n\n")
print(json.dumps(ai.get_related_articles_and_summary(article.maintext), indent = 4))