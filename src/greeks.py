# CALCULATE GREEKS FOR OPTIONS - DELTA, THETA, GAMMA, VEGA
import yfinance as yf
import pandas as pd
import numpy as np
from scipy.stats import norm





# The Greeks come from the Black-Scholes option pricing model.
def calc_greeks(options_df, current_price, user_expiration, option_type):
    s = current_price
    k = options_df["strike"]
    t = user_expiration / 365
    sigma = options_df["impliedVolatility"]
    r = 0.05

    # d1 and d2 formulas
    d1 = (np.log(s / k) + (r + sigma ** 2 / 2) * t) / (sigma * np.sqrt(t))
    d2 = d1 - sigma * np.sqrt(t)

    # calculate Delta
    if option_type == "call":
        options_df["delta"] = norm.cdf(d1)
    else:
        options_df["delta"] = norm.cdf(d1) - 1

    # calculate Gamma
    options_df["gamma"] = norm.pdf(d1) / (s * sigma * np.sqrt(t))

    # calculate Vega
    options_df["vega"] = s * norm.pdf(d1) * np.sqrt(t)

    # calculate Theta
    if option_type == "call":
        options_df["theta"] = (
                -(s * norm.pdf(d1) * sigma) / (2 * np.sqrt(t))
                - r * k * np.exp(-r * t) * norm.cdf(d2)
        )
    else:
        options_df["theta"] = (
                -(s * norm.pdf(d1) * sigma) / (2 * np.sqrt(t))
                + r * k * np.exp(-r * t) * norm.cdf(-d2)
        )
    # convert annual theta to daily
    options_df["theta"] = options_df["theta"] / 365

    # round the greeks
    options_df["delta"] = options_df["delta"].round(3)
    options_df["gamma"] = options_df["gamma"].round(4)
    options_df["vega"] = options_df["vega"].round(2)
    options_df["theta"] = options_df["theta"].round(2)
    return options_df
