from flask import Flask, request, jsonify
import joblib
from flask_cors import CORS # 👈 1. IMPORT THIS

app = Flask(__name__)
CORS(app) # 👈 2. INITIALIZE CORS


# Load the trained model and vectorizer
try:
    model = joblib.load('model.pkl')
    vectorizer = joblib.load('vectorizer.pkl')
except Exception as e:
    print(f"Error loading model or vectorizer: {e}")
    model = None
    vectorizer = None

@app.route('/predict', methods=['POST'])
def predict():
    if not model or not vectorizer:
        return jsonify({'error': 'Model not loaded properly'}), 500

    try:
        data = request.get_json()
        text_to_predict = [data['text']]
        
        vectorized_text = vectorizer.transform(text_to_predict)
        prediction_proba = model.predict_proba(vectorized_text)[0]
        
        positive_score = prediction_proba[1]
        sentiment = "Positive" if positive_score > 0.5 else "Negative"
        
        response = {
            'prediction': sentiment,
            'score': float(positive_score)
        }
        return jsonify(response)
        
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)