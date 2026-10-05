import re
from nltk.corpus import stopwords
import nltk 
from nltk.tokenize import word_tokenize

nltk.download('punkt_tab')
nltk.download('stopwords')

stop_words = set(stopwords.words('english'))
def clean_text(text):
    # 1. Remove HTML tags
    text = re.sub(r'<[^>]+>', ' ', text)
    
    # 2. Lowercase
    text = text.lower()
    
    # 3. Expand contractions (don't → do not)
    text = re.sub(r"n't", " not", text)
    
    # 4. Remove punctuation (keep ! and ?)
    text = re.sub(r'[^\w\s!?]', '', text)
    
    # 5. Remove numbers
    text = re.sub(r'\d+', '', text)
    
    # 6. Tokenize
    tokens = word_tokenize(text)
    
    # 7. Remove stopwords (but keep negations)
    negations = {'not', 'no', 'never', 'none', 'nobody', 'nothing'}
    tokens = [w for w in tokens if w not in stop_words or w in negations]
    
    return ' '.join(tokens)