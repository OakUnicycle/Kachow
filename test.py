BASE_ARTICLE_SUMMARY = """
The Bank of England today announced a surprise 0.5% cut in interest rates,
citing concerns about slowing economic growth and global market volatility.
Governor Andrew Bailey said the move was necessary to support households
and businesses during a period of uncertainty.
"""

SEARCH_RESULTS = [
  {
    "title": "Bank of England cuts rates in shock move - BBC News",
    "snippet": "The Bank of England has cut its main interest rate to 0.25% from 0.75%... Governor Andrew Bailey...",
    "link": "https://www.bbc.com/news/business-51838118"
  },
  {
    "title": "Log in - Bank of England",
    "snippet": "Please enter your credentials to access the secure Bank of England portal.",
    "link": "https://secure.bankofengland.co.uk/login"
  },
  {
    "title": "Andrew Bailey's best biscuit recipe - The Times",
    "snippet": "The Governor of the Bank of England shares his secret for the perfect shortbread...",
    "link": "https://www.thetimes.co.uk/food/andrew-bailey-recipe"
  },
  {
    "title": "UK market turmoil: What happens after a rate cut?",
    "snippet": "Following the Bank's decision, the pound sterling fell against the dollar as markets...",
    "link": "https://www.reuters.com/markets/uk-turmoil-rate-cut-2025"
  },
  {
    "title": "Economic Growth: What It Is, How It's Measured - Investopedia",
    "snippet": "Economic growth is an increase in the production of goods and services... Learn about GDP...",
    "link": "https.www.investopedia.com/terms/e/economicgrowth.asp"
  }
]

import openai_integration as ai

ai.verify_related(BASE_ARTICLE_SUMMARY, SEARCH_RESULTS)