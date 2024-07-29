from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Load the models and label encoder
with open('regressor.pkl', 'rb') as file:
    regressor = pickle.load(file)

# with open('classifier.pkl', 'rb') as file:
#     classifier = pickle.load(file)

# with open('label_encoder.pkl', 'rb') as file:
#     label_encoder = pickle.load(file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict_regression', methods=['POST'])
def predict_regression():
    length1 = float(request.form['length1'])
    length2 = float(request.form['length2'])
    length3 = float(request.form['length3'])
    height = float(request.form['height'])
    width = float(request.form['width'])
    features = np.array([[length1, length2, length3, height, width]])
    prediction = regressor.predict(features)
    result = f'The predicted weight of the fish is {prediction[0]:.2f} grams'
    return render_template('index.html', result=result)

# @app.route('/predict_classification', methods=['POST'])
# def predict_classification():
#     length1 = float(request.form['length1'])
#     length2 = float(request.form['length2'])
#     length3 = float(request.form['length3'])
#     height = float(request.form['height'])
#     width = float(request.form['width'])
#     features = np.array([[length1, length2, length3, height, width]])
#     prediction = classifier.predict(features)
#     species = label_encoder.inverse_transform(prediction)
#     result = f'The predicted species of the fish is {species[0]}'
#     return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
