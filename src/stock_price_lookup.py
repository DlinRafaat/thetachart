import yfinance as yf

def get_price(pick_ticker):
    ticker = yf.Ticker(pick_ticker.upper().strip())
    return ticker.fast_info["last_price"]