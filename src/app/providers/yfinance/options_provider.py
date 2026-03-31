import yfinance as yf
import streamlit as st
import pandas as pd
from datetime import date, datetime
from src.app.providers.yfinance.stock_provider import get_price
from src.app.core.calculations.greeks import calc_greeks
from src.app.core.filters.option_filters import get_nearby_strikes
pd.set_option('display.max_columns', None)


@st.cache_data(ttl=60)
def get_options_data(user_ticker, user_expiration, calls_or_puts, strike_num):
    ticker = yf.Ticker(user_ticker)
    expiration = ticker.options[user_expiration]
    expiration_date = datetime.strptime(expiration, "%Y-%m-%d").date()
    days_to_expiration = max((expiration_date - date.today()).days, 1)
    chain = ticker.option_chain(expiration)
    calls = chain.calls
    puts = chain.puts
    calls = calls[["lastPrice", "ask", "bid", "strike", "impliedVolatility", "volume", "openInterest"]]
    puts = puts[["lastPrice", "ask", "bid", "strike", "impliedVolatility", "volume", "openInterest"]]
    current_price = get_price(user_ticker)


    # give num of strike the user selects
    nearby_calls = get_nearby_strikes(calls, current_price, below=strike_num//2, above=strike_num//2)
    nearby_puts = get_nearby_strikes(puts, current_price, below=strike_num//2, above=strike_num//2)

    # fill any N/A values with "--"
    nearby_calls = nearby_calls.fillna({"volume": "--"})
    nearby_puts = nearby_puts.fillna({"volume": "--"})


    # ---CALCULATE GREEKS FOR OPTIONS - DELTA, THETA, GAMMA, VEGA---
    calls = calc_greeks(nearby_calls, current_price, days_to_expiration, "call")
    puts = calc_greeks(nearby_puts, current_price, days_to_expiration, "put")


    # return get_options_data
    # return get_options_data
    if calls_or_puts == 1:
        return {"calls": calls}
    elif calls_or_puts == 2:
        return {"puts": puts}
    else:
        return {"calls": calls, "puts": puts}
