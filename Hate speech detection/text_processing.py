import nltk
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer

nltk.download('punkt')
nltk.download('stopwords')

stemmer = SnowballStemmer("english")
stopword = set(stopwords.words("english"))

def tokenize_stem(text):
    tokens = nltk.word_tokenize(text)
    tokens = [word for word in tokens if word not in stopword]
    tokens = [word for word in tokens if word.isalpha()]
    tokens = [stemmer.stem(word) for word in tokens]
    return tokens
