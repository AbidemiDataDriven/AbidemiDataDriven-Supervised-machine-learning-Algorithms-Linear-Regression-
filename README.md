

# Fire Weather Index Prediction Web App

A simple **Flask web application** that predicts fire weather index (FWI) values using a trained **Ridge Regression model**. The app takes environmental and meteorological parameters as input and outputs a predicted FWI value.

---

## 🛠 Features

* User-friendly web interface with input form
* Predicts fire risk based on:

  * Temperature
  * Relative Humidity (RH)
  * Wind Speed (Ws)
  * Rainfall (Rain)
  * Forest Fire Weather Indices (FFMC, DMC, ISI)
  * Class and Region
* Scales input data automatically before prediction
* Returns the predicted FWI value

---

## 💻 Tech Stack

* Python 3.x
* Flask
* scikit-learn
* NumPy & Pandas
* HTML (for templates)
* Pickle (for loading trained model and scaler)

---

## 🚀 Installation

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/fire-weather-index-app.git
cd fire-weather-index-app
```

2. **Create and activate a virtual environment (optional but recommended)**

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Ensure models are in place**

Place the pre-trained model and scaler inside a `models/` folder:

```
models/
 ├── ridge.pkl
 └── scaler.pkl
```

5. **Run the app**

```bash
python app.py
```

The application will be available at https://abidemidatadriven-supervised-machine-1c28.onrender.com/predictdata

---

## 📂 Project Structure

```
fire-weather-index-app/
│
├── models/
│   ├── ridge.pkl       # Pre-trained Ridge Regression model
│   └── scaler.pkl      # StandardScaler object
│
├── templates/
│   ├── index.html      # Landing page
│   └── home.html       # Prediction result page
│
├── app.py              # Flask application
└── requirements.txt    # Python dependencies
```

---

## 📝 Usage

1. Open the web app in your browser.
2. Fill in the input fields:

   * Temperature
   * Relative Humidity (RH)
   * Wind Speed (Ws)
   * Rainfall (Rain)
   * FFMC, DMC, ISI
   * Class
   * Region
3. Click **Predict**.
4. View the predicted Fire Weather Index on the results page.

---

## ⚠️ Notes

* Ensure input values are numeric where required.
* The model and scaler files must match the trained versions used in the app.
* The app uses `debug=True` by default; turn it off for production.

---

<img width="1274" height="845" alt="Screenshot 2025-11-17 at 3 10 06 PM" src="https://github.com/user-attachments/assets/5626d0e8-8455-4b7c-ad4b-c6d3b74b0243" />



https://abidemidatadriven-supervised-machine-1c28.onrender.com/predictdata



