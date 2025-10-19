import gensim.downloader as api
import joblib

wv = api.load('word2vec-google-news-300')
filename = './word_rating_predictor.joblib'
joblib.dump(wv, filename)