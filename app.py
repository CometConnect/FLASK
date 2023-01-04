from flask import Flask, render_template, request
from text_sentiment_prediction import *

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
 
@app.route('/predict-emotion', methods=["POST"])
def predict_emotion():
    try:
        text = list(request.form)[0]
    except IndexError:
        text = ""

    if not text:
        return "Unknown::Unknown"

    return predict(text)

if __name__ == "__main__":
    app.run(debug=True)