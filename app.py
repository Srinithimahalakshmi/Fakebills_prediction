from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load("model/knn_model.pkl")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        features = [
            float(request.form['diagonal']),
            float(request.form['height_left']),
            float(request.form['height_right']),
            float(request.form['margin_low']),
            float(request.form['margin_up']),
            float(request.form['length'])
        ]
        prediction = model.predict([features])[0]
        result = "Genuine" if prediction == 1 else "Fake"
        return render_template('index.html', prediction_text=f"The Bank Note is: {result}")
    except Exception as e:
        return render_template('index.html', prediction_text=f"Error: {str(e)}")

if __name__ == "__main__":
    app.run(debug=True)
