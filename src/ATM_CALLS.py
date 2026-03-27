import yfinance as yf


def get_atm_call(user_ticker, user_expiration, calls_or_puts):

    ticker = yf.Ticker(user_ticker.strip())

    price = ticker.history(period="1d")["Close"].iloc[-1]

    expiration = ticker.options[user_expiration]

    calls = ticker.option_chain(expiration).calls
    puts = ticker.option_chain(expiration).puts

    calls["distance"] = abs(calls["strike"] - price)
    puts["distance"] = abs(puts["strike"] - price)


    if calls_or_puts == 1:
        calls_atm = calls.sort_values("distance").iloc[0]

        return calls_atm
    elif calls_or_puts == 2:
        puts_atm = puts.sort_values("distance").iloc[0]
        print(f"{user_ticker} PUTS OPTIONS")
        print(puts_atm)
    else:
        calls_atm = calls.sort_values("distance").iloc[0]
        puts_atm = puts.sort_values("distance").iloc[0]
        print()
        print(f"{user_ticker} CALLS OPTIONS")
        return calls_atm
