from flask import Flask, render_template, request, jsonify
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import json
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

# Download required NLTK data
nltk.download('vader_lexicon')

app = Flask(__name__)

def analyze_sentiment(text):
    sia = SentimentIntensityAnalyzer()
    sentiment_scores = sia.polarity_scores(text)
    
    # Determine overall sentiment
    compound_score = sentiment_scores['compound']
    if compound_score >= 0.05:
        sentiment = 'Positive'
    elif compound_score <= -0.05:
        sentiment = 'Negative'
    else:
        sentiment = 'Neutral'
    
    return {
        'sentiment': sentiment,
        'scores': sentiment_scores,
    }

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    if request.method == 'POST':
        data = request.get_json()
        text = data.get('text', '')
        
        if not text:
            return jsonify({'error': 'No text provided'}), 400
        
        result = analyze_sentiment(text)
        return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, port=8080) 