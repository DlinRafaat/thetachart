# ---- Get info on STOCKS ---- (vol. 52 week high/low, dividend, etc..)
import yfinance as yf

def get_stock_info(stock_ticker):
    stock_ticker = stock_ticker.upper()
    stock_ticker = yf.Ticker(stock_ticker)
    get_ticker_info = yf.Ticker.get_fast_info(stock_ticker)

# not working - fix -
def get_stock_news(stock_ticker):
    stock_ticker = stock_ticker.upper()
    stock_ticker = yf.Ticker(stock_ticker)
    get_ticker_info = yf.Ticker.get_news(stock_ticker)

ticker = input("Enter ticker: ")
print(get_stock_news(ticker))
