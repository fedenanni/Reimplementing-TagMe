import pickle,codecs, nltk,string
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
from scipy import sparse
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from sklearn.metrics.pairwise import cosine_similarity

wordnet_lemmatizer = WordNetLemmatizer()

exclude = set(string.punctuation)
stop_word_list = stopwords.words('english')

def nlp_pipeline_for_tfidf(text):
    
    text = nltk.word_tokenize(text)
    
    text = [wordnet_lemmatizer.lemmatize(token.lower()) for token in text]
    
    text = [token for token in text if token not in exclude and token.isalpha()]
    
    text = [token for token in text if token not in stop_word_list]

    return [" ".join(text)]


with open('Resources/tfidf_asps.pkl', 'rb') as f:
    tfidf_vectorizer = pickle.load(f, encoding='latin1')

def tfidf_cs(context, aspect):
    
    context = get_tfidf(context)
    aspect = get_tfidf(aspect)
    score = cos_sim(context,aspect)
    return score

def get_tfidf(sent):
    sent = sent.replace("_", " ")
    sent = nlp_pipeline_for_tfidf(sent)
    try:
        sent = tfidf_vectorizer.transform(sent)
        return sent
    except Exception as e:
        pass
    
def cos_sim(context, aspect):
    try:
        cs = cosine_similarity(context,aspect)[0][0]
        return cs
    except Exception as e:
        return 0.0
    
def rank(context, candidates):
    
    ranking = []
    
    for id_cand,content in candidates.items():
            id_cand = id_cand.replace(" ","_")
            content = " ".join(content)
            score = tfidf_cs(context,content)
            ranking.append([id_cand, score])
    ranking.sort(key=lambda k: (k[1]), reverse=True)
    return ranking