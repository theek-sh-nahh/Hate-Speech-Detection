from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
from text_processing import tokenize_stem

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

# Load the sentiment analysis model and vectorizer
model = joblib.load('sentiment_model.joblib')
vectorizer = joblib.load('vectorizer.joblib')

@app.route('/analyze', methods=['POST'])
def analyze_sentiment():
    data = request.get_json()
    text = data.get('text', '')

    if not text:
        return jsonify({'error': 'No text provided'}), 400

    sentiment = classify_tweet(text)
    return jsonify({'sentiment': sentiment})

def classify_tweet(tweet):
    tweet_vector = vectorizer.transform([tweet])
    prediction = model.predict(tweet_vector)
    label_map = {0: "Neutral", 1: "Offensive", 2: "Not Offensive"}
    return label_map[prediction[0]]

if __name__ == '__main__':
    app.run(debug=True)
