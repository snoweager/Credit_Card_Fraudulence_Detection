# Credit_Card_Fraudulence_Detection

# Overview

Credit card fraud is a persistent and evolving threat that affects millions of users and financial institutions worldwide. Traditional detection systems often struggle to adapt to sophisticated fraud patterns. This project aims to address that gap by using **machine learning** to build a robust, scalable, and intelligent fraud detection system, complete with a **Streamlit-powered web interface** for real-time predictions.

---

# Project Highlights

* Objective: Detect fraudulent credit card transactions using machine learning models trained on historical transaction data.
* Models Used:

  * Logistic Regression
  * Random Forest
  * XGBoost
  * Neural Networks
* Web App: Developed with Streamlit, allowing users to input transaction details and receive real-time fraud predictions.
* Secondary Utility: Includes a dataset viewer for analyzing incident patterns by insured occupation and sex.

---

## 📁 Files in this Repository

| File                            | Description                                                                  |
| ------------------------------- | ---------------------------------------------------------------------------- |
| `app.py`                        | Main Streamlit app for fraud detection and data viewer                       |
| `model_and_data.pkl`            | Pickled ML model used for prediction                                         |
| `logistic_regression_model.pkl` | Alternative model (e.g., Logistic Regression)                                |
| `exportt.csv`                   | Dataset for data viewer functionality (make sure it's in the same directory) |

---

# How to Run the Application

### 1. Clone the Repository

```bash
git clone https://github.com/your-repo/credit-card-fraud-detection.git
cd credit-card-fraud-detection
```

# 2. Install Requirements

```bash
pip install -r requirements.txt
```

If `requirements.txt` is not present, manually install:

```bash
pip install streamlit pandas scikit-learn xgboost joblib
```

# 3. Start the Streamlit App

```bash
streamlit run app.py
```

---

## App Features

# Fraud Detection Interface

* Input 5 key transaction features (can be extended)
* Real-time prediction: "Fraudulent" or "Not Fraudulent"
* Model automatically scales the input data before prediction

# Dataset Viewer

* Filters data by insured occupation and sex
* Displays related incident details:

  * Incident type, severity
  * Authorities contacted
  * City and police report status
  * Fraud report status

---

# Machine Learning Approach

1. Data Preprocessing

   * Feature scaling
   * Handling class imbalance
2. Model Training

   * Trained and evaluated multiple models
   * Selected best-performing model based on F1-score and AUC
3. Model Deployment

   * Model and scaler saved using `joblib`
   * Integrated into Streamlit for interactive use

---

## 📄 License

This project is licensed under the [GNU Affero General Public License v3.0](LICENSE).

---
