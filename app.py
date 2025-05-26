import streamlit as st
import numpy as np

# --- TITLE ---
st.title("📈 AAPL Next-Day Price Predictor")
st.markdown("""
This app predicts the **next-day closing price of AAPL stock** based on today's trading data and Reddit sentiment.
""")

# --- USER INPUT FORM ---
st.header("📝 Enter Today's Data")
with st.form("prediction_form"):
    open_price = st.number_input("Open Price", value=170.00, format="%.2f")
    high_price = st.number_input("High Price", value=171.00, format="%.2f")
    low_price = st.number_input("Low Price", value=169.00, format="%.2f")
    volume = st.number_input("Volume", value=50000000)
    sentiment = st.slider("Reddit Sentiment Score", min_value=-1.0, max_value=1.0, value=0.0, step=0.01)

    submitted = st.form_submit_button("Predict Price")

# --- MANUAL MODEL WEIGHTS (replace these later with real ones from your notebook) ---
w = np.array([
    [25.7],     # Bias
    [0.45],     # Open
    [-0.12],    # High
    [0.32],     # Low
    [0.000002], # Volume
    [1.5]       # Sentiment
])

# --- MAKE PREDICTION ---
if submitted:
    x_input = np.array([[1, open_price, high_price, low_price, volume, sentiment]])  # Add bias term
    predicted_price = x_input.dot(w)[0][0]

    st.success(f"📊 Predicted Next-Day Closing Price: **${predicted_price:.2f}**")
