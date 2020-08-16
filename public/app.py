from flask import Flask, render_template, url_for, request
import pandas as pd
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.externals import joblib

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    df = pd.read_csv('spam.csv', encoding="latin-1")

    # cleaning up the dataframe
    df['label'] = df['v1'].map({'ham': 0, 'spam': 1})
    df['message'] = df['v2']
    df.drop(['v1', 'v2', 'Unnamed: 2', 'Unnamed: 3',
             'Unnamed: 4'], axis=1, inplace=True)

    # create variables to hold the features and labels
    X = df['message']
    y = df['label']

    # fit the feature data properly
    cv = CountVectorizer()
    X = cv.fit_transform(X)  # Fit the Data

    # split the training and testing data properly
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42)

    # the naive bayes classifier
    clf = MultinomialNB()

    # fit the training data
    clf.fit(X_train, y_train)

    # accuracy score after testing on the test data
    clf.score(X_test, y_test)

    if request.method == 'POST':
        message = request.form['message']
        data = [message]
        vect = cv.transform(data).toarray()
        my_prediction = clf.predict(vect)

    return render_template('prediction.html', prediction=my_prediction)


if __name__ == '__main__':
    app.run(debug=True)
