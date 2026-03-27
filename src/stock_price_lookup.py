import yfinance as yf
import streamlit as st

@st.cache_data(ttl=60)
def get_price(pick_ticker):
    ticker = yf.Ticker(pick_ticker.upper().strip())
    return ticker.fast_info["last_price"]