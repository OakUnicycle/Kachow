# Kachow
## WHACK project
Bias scanner


## Setup instructions

First you need to get your own API keys - YOU CAN'T STEAL MINE.

### OpenAi

You need to get an openai API key, put money on your account and add the key to the .env file under OPENAI_API_KEY.

### Google Cloud

You need to set up a Custom Search API key for google cloud, this can be put in the .env file under GOOGLE_CLOUD_API_KEY along with the CSE id under CSE_ID.

### Installing requirements
```pip install -r requitements.txt```

### Running setup scripts
```python3 database.py```
```python3 creating_wv_model.py```

### Running the server
```python3 app.py```

You can then connect to this through the url specified.