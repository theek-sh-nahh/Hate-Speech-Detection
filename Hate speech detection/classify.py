import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import f1_score
import joblib
from text_processing import tokenize_stem

# Load the dataset
data = pd.read_csv("sentiment_dataset.csv")
data['labels'] = data['label'].map({"Neutral": 0, "Offensive": 1, "Not Offensive": 2})

# Initialize CountVectorizer with the custom tokenizer
vectorizer = CountVectorizer(tokenizer=tokenize_stem)
X = vectorizer.fit_transform(data['text'])

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, data['labels'], test_size=0.2, random_state=42)

# Initialize and train the Random Forest Classifier
classifier = RandomForestClassifier()
classifier.fit(X_train, y_train)

# Save the trained model and vectorizer to files
joblib.dump(classifier, 'sentiment_model.joblib')
joblib.dump(vectorizer, 'vectorizer.joblib')
