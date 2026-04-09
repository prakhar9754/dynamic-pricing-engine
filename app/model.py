import joblib
import numpy as np
import pandas as pd
import os

# Get project root directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  #base_dir = project root 

# Load models
clf_model = joblib.load(os.path.join(BASE_DIR, "models", "classification_model.pkl"))
reg_model = joblib.load(os.path.join(BASE_DIR, "models", "regression_model.pkl"))


def prepare_features(data):
    df = pd.DataFrame([data])
    
    # create log_price
    df['log_price'] = np.log1p(df['price'])
    
    return df


def predict(data):
    df = prepare_features(data)
    
    # Classification
    X_class = df.drop(columns=['price'])
    purchase_prob = clf_model.predict_proba(X_class)[:, 1][0]
    
    # Regression
    X_reg = df[reg_model.feature_names_in_]
    log_price_pred = reg_model.predict(X_reg)[0]
    predicted_price = np.expm1(log_price_pred)
    
    # Pricing logic
    if purchase_prob > 0.8:
        recommended_price = predicted_price * 1.15
    elif purchase_prob > 0.6:
        recommended_price = predicted_price * 1.08
    elif purchase_prob > 0.4:
        recommended_price = predicted_price
    elif purchase_prob > 0.2:
        recommended_price = predicted_price * 0.92
    else:
        recommended_price = predicted_price * 0.85
    
    return {
        "purchase_probability": round(float(purchase_prob), 4),
        "predicted_price": round(float(predicted_price), 2),
        "recommended_price": round(float(recommended_price), 2)
    }