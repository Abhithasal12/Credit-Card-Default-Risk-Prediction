import pandas as pd
import joblib

def load_model(model_path):
    """Load the trained model from the specified path."""
    model = joblib.load(model_path)
    return model_path

def predict(model, input_data):
    df = pd.DataFrame([input_data])
    prob = model.predict_proba(df)[1][0]
    return prob

def risk_category(prob):
    if prob < 0.3:
        return "Low Risk"
    elif prob < 0.6:
        return "Medium Risk"
    else:
        return "High Risk"
    

import feature_engineering
print(feature_engineering.__file__)
