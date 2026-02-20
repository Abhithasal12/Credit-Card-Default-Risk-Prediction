Credit Card Default Risk Prediction
Project Overview

This project predicts whether a credit card customer is likely to default on their next payment.
The goal is to help financial institutions assess risk and make better lending decisions.

The model is trained using historical credit data and deployed using a Streamlit web application.

Problem Statement

Credit card default is a major risk for banks and financial institutions.
Using customer financial and repayment history, we aim to predict the probability of default.

This is a binary classification problem:

. 0 → No Default

. 1 → Default

Dataset

. Source: Kaggle – UCI Credit Card Default Dataset

. Contains 30,000 customer records

. Includes demographic, billing, and payment history features

Features Used
Customer Information

. LIMIT_BAL (Credit Limit)

. SEX

. EDUCATION

. MARRIAGE

. AGE

Repayment Status (Past 6 Months)

. PAY_1 to PAY_6

Bill Amounts

. BILL_AMT1 to BILL_AMT6

Payment Amounts

. PAY_AMT1 to PAY_AMT6

Engineered Features

. Avg_pay_amt → Average payment amount

. Avg_bill_pay → Average bill amount

. Max_Delay → Maximum repayment delay

Model Used

Logistic Regression

Why Logistic Regression?

. Simple and interpretable

. Suitable for binary classification

. Performs well on structured financial data

. Easy to explain in interviews

Model Evaluation

Evaluation metrics used:

. Accuracy

. Confusion Matrix

. ROC-AUC Score

The model was trained using properly aligned features and saved using joblib.

Project Structure

project/
│
├── app.py
├── feature_engineering.py
├── model/
│   ├── credit_default_model.pkl
│   └── features.pkl
├── notebook.ipynb
└── README.md

How to Run the Project

1. Install dependencies
pip install -r requirements.txt

2. Run the Streamlit app
streamlit run app.py

Skills Demonstrated

. Data Cleaning

. Feature Engineering

. Classification Modeling

. Model Saving and Loading

. Streamlit Deployment

. End-to-End ML Pipeline Design


Author

Abhishek Thasal
Aspiring Data Scientist