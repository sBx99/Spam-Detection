from flask import Flask, jsonify, render_template, request
import numpy as np
import joblib

def create_app(test_config=None):

    app = Flask(__name__)

    @app.route("/")
    def index():
        return render_template("index.html")

    @app.route('/predict', methods=['POST'])
    def predict():
        try:
            text = request.form.get("text")

            clf_pipeline = joblib.load('model.pkl')
            result = "Spam" if clf_pipeline.predict([text])[0] else "Ham"
            probability  = np.max(clf_pipeline.predict_proba([text]))

            return jsonify(result=result, probability=round(probability*100, 2)), 200
        
        except Exception as error:
            return jsonify(error=str(error)), 500

    return app
