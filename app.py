from flask import Flask, render_template, request, jsonify
import numpy as np
import pickle
import json
from datetime import datetime
import os

app = Flask(__name__)

# Load the trained model
model = pickle.load(open("static/model.pkl", "rb"))

# Create predictions directory if it doesn't exist
if not os.path.exists('predictions'):
    os.makedirs('predictions')

# Initialize or load the predictions JSON file
predictions_file = 'predictions/transaction_predictions.json'
if not os.path.exists(predictions_file):
    with open(predictions_file, 'w') as f:
        json.dump([], f)

def load_predictions():
    try:
        with open(predictions_file, 'r') as f:
            return json.load(f)
    except:
        return []

def save_prediction(prediction_data):
    predictions = load_predictions()
    predictions.append(prediction_data)
    with open(predictions_file, 'w') as f:
        json.dump(predictions, f, indent=4)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input values from the form
        type = request.form['type']
        amount = float(request.form['amount'])
        oldbalanceOrg = float(request.form['oldbalanceOrg'])
        newbalanceOrig = float(request.form['newbalanceOrig'])

        # Map transaction types to numeric values
        type_mapping = {
            "CASH_OUT": 1,
            "PAYMENT": 2,
            "CASH_IN": 3,
            "TRANSFER": 4,
            "DEBIT": 5
        }
        val = type_mapping.get(type, 5)  # Default to 5 if type not found

        # Create input array for prediction
        input_array = np.array([[val, amount, oldbalanceOrg, newbalanceOrig]])

        # Make prediction using the loaded model
        prediction = model.predict(input_array)
        result = "Fraudulent Transaction" if prediction[0] == 1 else "Legitimate Transaction"

        # Create prediction data
        prediction_data = {
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'transaction_details': {
                'type': type,
                'amount': amount,
                'old_balance': oldbalanceOrg,
                'new_balance': newbalanceOrig
            },
            'prediction': {
                'result': result,
                'is_fraud': bool(prediction[0])
            }
        }

        # Save prediction to JSON file
        save_prediction(prediction_data)

        return render_template('index.html', 
                            prediction_text=result,
                            saved_message="Prediction saved to predictions/transaction_predictions.json")

    except Exception as e:
        return render_template('index.html', prediction_text=f"Error: {str(e)}")

@app.route('/predictions', methods=['GET'])
def get_predictions():
    predictions = load_predictions()
    return jsonify(predictions)

if __name__ == '__main__':
    app.run(debug=True, port=8080)
