import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

nltk.download('stopwords')
nltk.download('wordnet')

stop = set(stopwords.words('english'))
lemma = WordNetLemmatizer()

def clean_text(text):
    text = text.lower()
    text = re.sub(r"http\S+", " ", text) 
    text = re.sub(r"<.*?>", " ", text)     
    text = text.replace("|||", " ")   
    text = re.sub(r"[^a-z\s]", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()

def preprocess(text):
    text = clean_text(text)
    tokens = text.split()
    tokens = [w for w in tokens if w not in stop]
    tokens = [lemma.lemmatize(w) for w in tokens]
    return " ".join(tokens)

mbti_types = ["intj","intp","entj","entp","infj","infp","enfj","enfp","istj","istp","estj","estp","isfj","isfp","esfj","esfp"]
def remove_mbti_words(text):
    for t in mbti_types:
        text = text.replace(t, "")
        text = text.replace(t.upper(), "")
    return text

def remove_cog_functions(text):
    return re.sub(r'\b(ne|ni|se|si|te|ti|fe|fi)\b', ' ', text)

def full_preprocess(text):
    text = preprocess(text)
    text = remove_mbti_words(text)
    text = remove_cog_functions(text)
    text = re.sub(r"\s+", " ", text).strip()
    return text