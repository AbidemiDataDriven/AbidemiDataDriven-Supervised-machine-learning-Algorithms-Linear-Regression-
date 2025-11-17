from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Ridge
import warnings
warnings.filterwarnings("ignore", category=UserWarning)
warnings.filterwarnings("ignore", category=FutureWarning)

application = Flask(__name__)
app = application

# Load model and scaler
ridge = pickle.load(open('models/ridge.pkl', 'rb'))
standard_scaler = pickle.load(open('models/scaler.pkl', 'rb'))

# Home page
@app.route('/')
def index():
    return render_template('index.html')

# Prediction route
@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():

    if request.method == 'POST':

            # Extract inputs safely
            Temperature = float(request.form.get('Temperature'))
            RH = float(request.form.get('RH'))
            Ws = float(request.form.get('Ws'))
            Rain = float(request.form.get('Rain'))
            FFMC = float(request.form.get('FFMC'))
            DMC = float(request.form.get('DMC'))
            ISI = float(request.form.get('ISI'))
            Classes = request.form.get('Classes')
            Region = request.form.get('Region')

            # Prepare input for model
            input_data = [[Temperature, RH, Ws, Rain, FFMC, DMC, ISI, Classes, Region]]

            # Scale data
            new_data_scaled = standard_scaler.transform(input_data)

            # Predict
            result = ridge.predict(new_data_scaled)

            # Return prediction
            return render_template('home.html', results=result[0])

    return render_template('home.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
