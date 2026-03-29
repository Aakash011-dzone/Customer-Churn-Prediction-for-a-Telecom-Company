# Customer-Churn-Prediction-for-a-Telecom-Company

📊 Customer Churn Prediction for Telecom Company

🔹 Project Overview

This project aims to predict customer churn in a telecom company using Machine Learning.
Customer churn refers to customers leaving the service provider. By predicting churn, companies can take proactive steps to retain customers.


🎯 Problem Statement

A telecom company is experiencing high customer churn, leading to revenue loss.
The objective is to build a machine learning model that can identify customers who are likely to churn based on their behavior and service usage.


📂 Dataset Description

The dataset contains customer-related information such as:

Age

Gender

Tenure (duration with company)

Usage Frequency

Support Calls

Payment Delay

Subscription Type

Contract Length

Total Spend

Last Interaction

Churn (Target Variable)


⚙️ Methodology

1️⃣ Data Preprocessing

Handled categorical variables using Label Encoding

Standardized numerical features using StandardScaler


2️⃣ Model Building

Used Random Forest Classifier

Split data into training and validation sets

Achieved high prediction accuracy


3️⃣ Model Evaluation

Accuracy Score

Confusion Matrix

Classification Report


4️⃣ Model Saving

Saved trained model using joblib

Saved scaler for consistent preprocessing


🤖 Machine Learning Model

Algorithm Used: Random Forest

Reason: Handles non-linear data, reduces overfitting, and provides high accuracy


🌐 Deployment (Streamlit App)

The model is deployed using Streamlit to provide an interactive web interface.

Features:

User-friendly input form

Real-time churn prediction

Displays churn probability


🚀 How to Run the Project

Step 1: Install Dependencies

pip install -r requirements.txt

Step 2: Run the App

streamlit run app.py


📈 Output

The system predicts:

✅ Customer likely to stay

⚠️ Customer likely to churn

📊 Churn probability (%)



💡 Business Use Case

This system helps telecom companies:

Identify high-risk customers

Improve customer retention strategies

Reduce revenue loss


📚 Learning Outcomes

Data preprocessing and feature engineering

Machine learning model building (Random Forest)

Model evaluation techniques

Deployment using Streamlit

Handling real-world datasets


🔗 Project Structure

Customer_Churn_Project/
│
├── app.py
├── churn_model.pkl
├── scaler.pkl
├── churn_training.ipynb
├── requirements.txt
├── README.md
└── data/
    ├── churn_train.csv
    └── churn_test.csv


* Conclusion

The project successfully predicts customer churn using machine learning and provides a practical solution for telecom companies to enhance customer retention.


