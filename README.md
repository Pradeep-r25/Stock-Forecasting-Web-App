# Stock Forecasting Web App (INR) 

A Streamlit-based stock prediction app for NSE stocks (**RELIANCE.NS, TCS.NS, HDFCBANK.NS, INFY.NS**) using Yahoo Finance data and Facebook Prophet. This app allows users to visualize stock trends, interact with real-time data, and forecast future prices. 🚀📈

## Features
- 📊 **Live Stock Data**: Fetches historical stock data from Yahoo Finance.
- 🔍 **Interactive Visualization**: Uses Plotly for time series graphs.
- 🔮 **Stock Price Forecasting**: Predicts future stock prices using Facebook Prophet.
- 🎛 **User-Controlled Predictions**: Select stock and forecast period via UI.
- 📈 **Detailed Forecast Components**: Breaks down forecasted trends and seasonality with Matplotlib.

---

## 🛠 Installation & Usage

### Prerequisites
Ensure you have **Python 3.7+** installed on your system.

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/Stock-Forecasting-Web-App.git
cd Stock-Forecasting-Web-App
```

### 2️⃣ Install Dependencies Manually
```bash
pip install streamlit pandas yfinance prophet plotly numpy matplotlib
```

### 3️⃣ Run the Streamlit App
```bash
streamlit run app.py
```

---

## 📜 How It Works
1. **Select a Stock**: Choose an NSE stock from the dropdown menu.
2. **Set Forecast Period**: Use the slider to define prediction years (1-4 years).
3. **View Raw Data**: Displays the latest stock data fetched from Yahoo Finance.
4. **Visualize Stock Trends**: Interactive time series charts for Open/Close prices.
5. **Forecast Future Prices**: Uses Facebook Prophet to predict future trends.
6. **Explore Forecast Components**: Breaks down trends, weekly/monthly seasonality.

---

## 📦 Project Structure
```
Stock-Forecasting-Web-App/
│── app.py                  # Main Streamlit app script
│── README.md               # Project documentation
│── .gitignore              # Ignore unnecessary files
```

---

## 📚 Technologies Used
- **Streamlit** → Web framework for interactive UI
- **Yahoo Finance (yfinance)** → Fetch stock market data
- **Facebook Prophet** → Time series forecasting
- **Plotly** → Interactive stock price visualization
- **Matplotlib & NumPy** → Custom forecasting component graphs

---

## 🏆 Contributing
Contributions are welcome! Feel free to fork this repository and submit pull requests. 💡🚀

1. **Fork** the repository
2. **Create a feature branch**: `git checkout -b feature-new`
3. **Commit changes**: `git commit -m "Add new feature"`
4. **Push to GitHub**: `git push origin feature-new`
5. **Create a Pull Request**

---


---

## 📞 Contact
For any queries or suggestions, feel free to reach out:
- 📧 Email: [pradeeprajkumar025@gmail.com]
- 🌍 GitHub: [Your GitHub Profile](https://github.com/Pradeep-r25)

---

_⭐ If you found this project useful, consider giving it a star! ⭐_

