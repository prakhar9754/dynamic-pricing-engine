# 💰 Dynamic Pricing Engine (End-to-End Machine Learning Project)

## 🚀 Project Overview

This project builds a **Dynamic Pricing Engine** that intelligently recommends product prices based on:

* User behavior
* Purchase probability
* Product-level insights

The system combines **Machine Learning + Business Logic** to simulate real-world pricing strategies used in e-commerce platforms.

---

## 🎯 Objective

To design an end-to-end system that:

* Predicts whether a user will purchase a product
* Estimates the optimal price for a product
* Recommends a final price to maximize revenue and conversions

---

## 🧠 Key Features

✅ Purchase Prediction (Classification Model)
✅ Price Prediction (Regression Model)
✅ Smart Pricing Strategy (Business Logic Layer)
✅ End-to-End ML Pipeline
✅ Clean modular notebooks

---

## 🏗️ Project Structure

```
Dynamic_Pricing_Engine/
│
├── data/
│   ├── final_featured_data.csv
│   ├── price_recommendations.csv
│
├── models/
│   ├── classification_model.pkl
│   ├── regression_model.pkl
│
├── notebooks/
│   ├── 01_problem_framing.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_feature_engineering.ipynb
│   ├── 04_model_training.ipynb
│   ├── 05_model_evaluation.ipynb
│   ├── 06_price_recommendation_engine.ipynb
```

---

## ⚙️ Workflow

### 1️⃣ Data Processing

* Cleaned raw e-commerce data
* Handled missing values and outliers
* Standardized categorical features

### 2️⃣ Feature Engineering

* Created behavioral features (user activity, conversion rate)
* Product-level statistics (mean price, std deviation)
* Log transformation for price (`log_price`)

### 3️⃣ Model Training

#### 🔹 Classification Model

* Predicts: **Will user purchase?**
* Algorithm: Logistic Regression

#### 🔹 Regression Model

* Predicts: **Optimal product price**
* Algorithm: Random Forest Regressor

---

### 4️⃣ Price Recommendation Engine

Combines:

* Purchase probability
* Predicted price

👉 Applies dynamic pricing strategy:

| Demand Level | Action         |
| ------------ | -------------- |
| High         | Increase price |
| Medium       | Keep price     |
| Low          | Apply discount |

---

## 📊 Sample Output

| Original Price | Predicted Price | Recommended Price | Purchase Probability |
| -------------- | --------------- | ----------------- | -------------------- |
| 500            | 520             | 560               | 0.82                 |
| 300            | 280             | 250               | 0.25                 |

---

## 💡 Key Learnings

* Importance of **feature consistency** between training and inference
* Handling **log transformations in regression models**
* Designing **end-to-end ML systems**, not just models
* Combining ML predictions with **business logic**

---

## 🚀 Business Impact

* 📈 Increase revenue through smart pricing
* ⚡ Enable data-driven pricing decisions

##

---

## 🛠️ Tech Stack

* Python
* Pandas, NumPy
* Scikit-learn
* Joblib

---

## 👨‍💻 Author

**Prakhar shrivastava**

---

## ⭐ If you found this useful

Give this project a ⭐ on GitHub!
