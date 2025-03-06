import streamlit as st
import pandas as pd
import yfinance as yf
from prophet import Prophet
from prophet.plot import plot_plotly
from plotly import graph_objs as go
from datetime import date
import numpy as np
import matplotlib.pyplot as plt

# Constants
START = "2015-01-01"
TODAY = date.today().strftime("%Y-%m-%d")

# Streamlit App Title
st.title('Stock Forecast App (INR)')

# Dropdown for Stock Selection (NSE Tickers)
stocks = ('RELIANCE.NS', 'TCS.NS', 'HDFCBANK.NS', 'INFY.NS') #added NSE Tickers
selected_stock = st.selectbox('Select dataset for prediction (NSE)', stocks)

# Slider for Prediction Years
n_years = st.slider('Years of prediction:', 1, 4)
period = n_years * 365

# Caching Data to Improve Performance
@st.cache_data
def load_data(ticker):
    """Loads stock data from Yahoo Finance."""
    data = yf.download(ticker, START, TODAY)
    data.reset_index(inplace=True)
    return data

# Load Data
data_load_state = st.text('Loading data...')
data = load_data(selected_stock)
data_load_state.text('Loading data... done!')

# Display Raw Data
st.subheader('Raw data (INR)')
st.write(data.tail())

# Plot Raw Data
def plot_raw_data():
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data['Date'], y=data['Open'], name="stock_open (₹)"))
    fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name="stock_close (₹)"))
    fig.layout.update(title_text=f'{selected_stock} Time Series data with Rangeslider (INR)', xaxis_rangeslider_visible=True)
    st.plotly_chart(fig)

plot_raw_data()

# Ensure the DataFrame Has Required Columns
if 'Date' not in data.columns or 'Close' not in data.columns:
    st.error("Error: Missing required columns in stock data.")
    st.stop()

# Prepare Data for Prophet
df_train = data[['Date', 'Close']].copy()
df_train.columns = ['ds', 'y']

df_train['y'] = pd.to_numeric(df_train['y'], errors='coerce')
df_train = df_train.dropna(subset=['y'])
df_train['y'] = df_train['y'].astype('float64')

# Prophet Model & Forecasting
m = Prophet()
m.fit(df_train)
future = m.make_future_dataframe(periods=period)
forecast = m.predict(future)

# Show Forecast Data
st.subheader('Forecast data (INR)')
st.write(forecast.tail())

# Plot Forecast
st.write(f'Forecast plot for {n_years} years (INR)')
fig1 = plot_plotly(m, forecast)
print(fig1)
st.plotly_chart(fig1)

# Show Forecast Components (Manual Plotting with NumPy)
st.write("Forecast components (INR)")

# Extract components and convert to NumPy arrays
components = [col for col in forecast.columns if col not in ['ds', 'yhat', 'yhat_lower', 'yhat_upper']]
ds_numpy = forecast['ds'].to_numpy() #convert the ds column to a numpy array.

# Create subplots
fig, axes = plt.subplots(len(components), 1, figsize=(10, 3 * len(components)))
if len(components) == 1:
    axes = [axes]  # Ensure axes is iterable

# Plot each component using NumPy arrays
for i, component in enumerate(components):
    component_numpy = forecast[component].to_numpy() #convert the component column to a numpy array.
    axes[i].plot(ds_numpy, component_numpy)
    axes[i].set_title(f'{component} (₹)')
    axes[i].set_xlabel('Date')

st.pyplot(fig)  # Display the Matplotlib figure in Streamlit