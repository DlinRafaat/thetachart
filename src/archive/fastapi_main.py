from fastapi import FastAPI

from src.app.providers.yfinance.stock_provider import get_price

app = FastAPI()

@app.get("/")
def root():
    return {"Testing NEW VERSIONS"}


@app.get("/price")
def price(symbol: str):
    current_price = get_price(symbol)
    return {
        "symbol": symbol.upper().strip(),
        "price": round(current_price, 2)
    }

@app.post("/ticker/")
def user_ticker(symbol: str, expiration: int):
    return {"symbol": symbol, "expiration:": expiration}

@app.put("/ticker/{symbol}")
def update_ticker(symbol: str, expiration: int):
    return {"symbol": symbol, "expiration:": expiration}
