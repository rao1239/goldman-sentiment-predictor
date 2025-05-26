### ✨ Credits
BUILT this AI model as a financial prediction ML project integrating NLP and regression.-Ansh Yadav

# 📈 AAPL Stock Price Predictor with Reddit Sentiment

This is a Streamlit-based web app that predicts the **next-day closing price of Apple Inc. (AAPL)** stock based on:
- Current day's stock data (Open, High, Low, Volume)
- Reddit sentiment analysis using VADER/TextBlob

### 🔍 What It Does
- Lets you input today’s trading data + Reddit sentiment score
- Uses a linear regression model trained from scratch (Normal Equation)
- Outputs a predicted closing price for the next trading day

---

### 🧠 Features Used
- Open Price
- High Price
- Low Price
- Volume
- **Reddit Sentiment Score** (from r/stocks, r/investing, r/wallstreetbets)

---

### ⚙️ Tech Stack
- Python
- Streamlit
- NumPy, Pandas
- TextBlob (or VADER)
- scikit-learn (for evaluation only)
- Manual matrix math using Normal Equation

---

### 📦 Run Locally

```bash
git clone https://github.com/yourusername/goldman-sentiment-predictor.git
cd goldman-sentiment-predictor
pip install -r requirements.txt
streamlit run app.py
