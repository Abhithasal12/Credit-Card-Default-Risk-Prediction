import streamlit as st
import joblib
import pandas as pd
from feature_engineering import calculate_avg_payment_column 

model = joblib.load('model/credit_default_model.pkl')
features_col = joblib.load('model/features.pkl')

st.title("Credit Card Default Risk Prediction")
st.subheader("Enter the details of the credit card holder")

with st.form("prediction_form"):
    LIMIT_BAL = st.number_input("Credit Limit", min_value=0, value=200000)
    SEX = st.selectbox("Sex", options=[1, 2]) # 1: male, 2: female
    EDUCATION = st.selectbox("Education", options=[1, 2, 3, 4]) # 1: graduate school, 2: university, 3: high school, 4: others
    MARRIAGE = st.selectbox("Marriage", options=[1, 2, 3]) # 1: married, 2: single, 3: others
    AGE = st.number_input("Age", min_value=18,max_value=100, value=30)

    PAY_1 = st.number_input("Repayment Status Sep (PAY_1)", value=0)
    PAY_2 = st.number_input("Repayment Status Aug (PAY_2)", value=0)
    PAY_3 = st.number_input("Repayment Status Jul (PAY_3)", value=0)
    PAY_4 = st.number_input("Repayment Status Jun (PAY_4)", value=0)
    PAY_5 = st.number_input("Repayment Status May (PAY_5)", value=0)
    PAY_6 = st.number_input("Repayment Status Apr (PAY_6)", value=0)

    BILL_AMT1 = st.number_input("Bill Amount 1", value=5000)
    BILL_AMT2 = st.number_input("Bill Amount 2", value=4000)
    BILL_AMT3 = st.number_input("Bill Amount 3", value=3000)
    BILL_AMT4 = st.number_input("Bill Amount 4", value=2000)
    BILL_AMT5 = st.number_input("Bill Amount 5", value=1000)
    BILL_AMT6 = st.number_input("Bill Amount 6", value=500)

    PAY_AMT1 = st.number_input("Payment Amount 1", value=2000)
    PAY_AMT2 = st.number_input("Payment Amount 2", value=2000)
    PAY_AMT3 = st.number_input("Payment Amount 3", value=2000)
    PAY_AMT4 = st.number_input("Payment Amount 4", value=2000)
    PAY_AMT5 = st.number_input("Payment Amount 5", value=2000)
    PAY_AMT6 = st.number_input("Payment Amount 6", value=2000)

    submit_button = st.form_submit_button("Predict")
if submit_button:

    user_input = {
        "LIMIT_BAL": LIMIT_BAL,
        "SEX": SEX,
        "EDUCATION": EDUCATION,
        "MARRIAGE": MARRIAGE,
        "AGE": AGE,
        "PAY_1": PAY_1,
        "PAY_2": PAY_2,
        "PAY_3": PAY_3,
        "PAY_4": PAY_4,
        "PAY_5": PAY_5,
        "PAY_6": PAY_6,
        "BILL_AMT1": BILL_AMT1,
        "BILL_AMT2": BILL_AMT2,
        "BILL_AMT3": BILL_AMT3,
        "BILL_AMT4": BILL_AMT4,
        "BILL_AMT5": BILL_AMT5,
        "BILL_AMT6": BILL_AMT6,
        "PAY_AMT1": PAY_AMT1,
        "PAY_AMT2": PAY_AMT2,
        "PAY_AMT3": PAY_AMT3,
        "PAY_AMT4": PAY_AMT4,
        "PAY_AMT5": PAY_AMT5,
        "PAY_AMT6": PAY_AMT6,
    }
    input_data = pd.DataFrame([user_input])

    input_data = calculate_avg_payment_column(input_data)

    input_data = input_data.reindex(columns = features_col, fill_value=0)

    prob = model.predict_proba(input_data)[0][1]
    st.write(f"Predicted Probability of Default: {prob:.2f}")