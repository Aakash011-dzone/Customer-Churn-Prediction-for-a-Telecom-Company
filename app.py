import streamlit as st
import numpy as np
import joblib

# Load model and scaler
model = joblib.load("churn_model.pkl")
scaler = joblib.load("scaler.pkl")

# Page config
st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊",
    layout="centered"
)

# Title
st.title("📊 Customer Churn Prediction System")
st.write(
    "This application predicts whether a customer is likely to **churn** "
    "based on usage, billing, and service behavior."
)

st.markdown("---")

# Sidebar for inputs
st.sidebar.header("🧾 Customer Details")

age = st.sidebar.slider("Age", 18, 80, 30)

gender = st.sidebar.selectbox("Gender", ["Male", "Female"])
gender = 1 if gender == "Male" else 0

tenure = st.sidebar.slider("Tenure (months)", 0, 72, 12)
usage_frequency = st.sidebar.slider("Usage Frequency", 0, 100, 50)
support_calls = st.sidebar.slider("Support Calls", 0, 20, 2)
payment_delay = st.sidebar.slider("Payment Delay (days)", 0, 30, 5)

subscription_type = st.sidebar.selectbox(
    "Subscription Type", ["Basic", "Standard", "Premium"]
)
subscription_type = {"Basic": 0, "Standard": 1, "Premium": 2}[subscription_type]

contract_length = st.sidebar.slider("Contract Length (months)", 1, 36, 12)
total_spend = st.sidebar.number_input(
    "Total Spend", min_value=0.0, value=5000.0
)
last_interaction = st.sidebar.slider(
    "Days Since Last Interaction", 0, 90, 10
)

# Prepare input
input_data = np.array([[
    age, gender, tenure, usage_frequency, support_calls,
    payment_delay, subscription_type, contract_length,
    total_spend, last_interaction
]])

input_scaled = scaler.transform(input_data)

# Prediction section
st.markdown("## 🔍 Prediction Result")

if st.button("Predict Churn"):
    prediction = model.predict(input_scaled)[0]
    probability = model.predict_proba(input_scaled)[0][1]

    if prediction == 1:
        st.error("⚠️ Customer is likely to **CHURN**")
    else:
        st.success("✅ Customer is likely to **STAY**")

    st.info(f"📈 Churn Probability: **{probability*100:.2f}%**")

st.markdown("---")
st.caption("Developed using Machine Learning & Streamlit")
