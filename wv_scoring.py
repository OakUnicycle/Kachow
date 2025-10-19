import string
import joblib
import nltk
nltk.download('stopwords')
nltk.download('wordnet')
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from newsplease import NewsPlease

class Bias_Score():
  LIBERAL_SEEDS = {'progressive', 'equity', 'regulation', 'diversity', 'taxation', 'environmental'}
  CONSERVATIVE_SEEDS = {'freedom', 'liberty', 'capitalism', 'deregulation', 'tradition', 'military'}
  POSITIVE_SEEDS = {'good', 'excellent', 'great', 'success', 'benefit', 'joy', 'wonderful'}
  NEGATIVE_SEEDS = {'bad', 'terrible', 'awful', 'failure', 'harm', 'pain', 'atrocity'}

  def __init__(self, url, wv_model):
    self.url = url
    self.model = wv_model
    self.lemmatizer = WordNetLemmatizer()
    self.stop_words = set(stopwords.words('english'))

  def extracting_raw_text(self):
      article = NewsPlease.from_url(self.url)
      if not article.maintext:
            raise ValueError("Article main text could not be extracted.")
      return article.maintext

  def preprocess_text(self, input_text):
    input_text = input_text.lower()
    input_text = input_text.translate(str.maketrans('', '', string.punctuation))
    seperated_text = input_text.split()
    processed_words = []
    for word in seperated_text:
      if word not in self.stop_words and word.isalpha():
        lemma = self.lemmatizer.lemmatize(word)
        processed_words.append(lemma)
    return list(set(seperated_text))

  def calculate_targeted_bias(self, article_words, target_seeds):
    article_words = [word for word in article_words if word in self.model.key_to_index]
    if not article_words:
      return 0.0
    valid_seeds = [word for word in target_seeds if word in self.model.key_to_index]
    if not valid_seeds:
      return 0.0

    total_similarity = 0
    valid_comparisons = 0

    for article_word in article_words:
        try:
            seed_similarities = [self.model.similarity(article_word, seed) for seed in valid_seeds]
            avg_seed_similarity = sum(seed_similarities) / len(valid_seeds)
                
            total_similarity += avg_seed_similarity
            valid_comparisons += 1
        except KeyError:
            pass
        
        if valid_comparisons > 0:
            return str(4*total_similarity / valid_comparisons)
        else:
            return str(0.0)
  
  def get_bias_scores(self, dictionary=None):
    try:
      raw_text = self.extracting_raw_text()
      article_words = self.preprocess_text(raw_text)
      if not article_words:
        return {'error': 'No significant words remained after preprocessing.'}
      
      if dictionary is not None:
        extra_scores = {}
        for key in dictionary:
          extra_scores[key] = self.calculate_targeted_bias(article_words, [key])
                
      scores = {}

      scores['liberal_affinity'] = self.calculate_targeted_bias(article_words, self.LIBERAL_SEEDS)
      scores['conservative_affinity'] = self.calculate_targeted_bias(article_words, self.CONSERVATIVE_SEEDS)
      scores['positive_sentiment'] = self.calculate_targeted_bias(article_words, self.POSITIVE_SEEDS)
      scores['negative_sentiment'] = self.calculate_targeted_bias(article_words, self.NEGATIVE_SEEDS)
            
      scores['political_bias_score'] = str( -float(scores['liberal_affinity']) + float(scores['conservative_affinity']))
      scores['sentiment_score'] = str(float(scores['positive_sentiment']) - float(scores['negative_sentiment']))
      if dictionary is not None:
        scores.update(extra_scores) 
      return scores
    except ValueError as e:
          return {'error': str(e)}
    except Exception as e:
          return {'error': f"An unexpected error occurred during scoring: {e}"}
    
def main(url, model, extra_arguments=None):
    instance = Bias_Score(url, model)
    extra_args_dict = None
    if extra_arguments is not None:
        extra_args_dict = {argument: 0 for argument in extra_arguments}  
    all_scores = instance.get_bias_scores(extra_args_dict)
    return all_scores

def getting_scores(url, arguments=None):
    filename = './word_rating_predictor.joblib'
    wv_model = joblib.load(filename)
    score = main(url, wv_model, arguments)
    return score 
