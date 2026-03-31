import yfinance as yf

from src.app.core.filters.option_filters import get_nearby_strikes, filter_volume, open_int, print_options
from src.app.providers.yfinance.stock_provider import get_price
from src.app.providers.yfinance.options_provider import get_options_data


# ask for ticker symbol, expiration date, and calls_or_puts
ticker = str(input("Enter stock ticker: "))
ticker = ticker.strip().upper()
expiration = int(input("Enter contract expiration date: "))
calls_puts = int(input("Enter (1) for calls: \nEnter (2) for puts: \nEnter (3) for both: "))

print(f"Current {ticker} price: ${get_price(ticker):.2f}")

strike_num = (int(input("How many strikes would you like to see?(default is 11): ")))

options_df = get_options_data(ticker, expiration, calls_puts, strike_num)
print_options(options_df, ticker)

filters = True

while filters:
    filter_selection = int(input("What filters would you like to apply to the options chain?\n"
                             "(1) Change amount of Strikes\n"
                             "(2) Filter by Volume\n"
                                "(3) Filter by Open Interest\n"
                                 "(4) No filters needed: "))
    if filter_selection == 1:
        strike_num = (int(input("How many strikes would you like to see?(default is 11): ")))
        options_df = get_options_data(ticker, expiration, calls_puts, strike_num)
        print_options(options_df, ticker)

    elif filter_selection == 2:
        volume_filter = int(input("Enter minimum volume: "))
        options_df = get_options_data(ticker, expiration, calls_puts, strike_num)
        for key in options_df:
            options_df[key] = filter_volume(options_df[key], volume_filter)
        print_options(options_df, ticker)

    elif filter_selection == 3:
        open_int_filter = int(input("Enter minimum open interest: "))
        options_df = get_options_data(ticker, expiration, calls_puts, strike_num)
        for key in options_df:
            options_df[key] = open_int(options_df[key], open_int_filter)
        print_options(options_df, ticker)

    elif filter_selection == 4:
        filters = False
        break
    else:
        print("Please select one: ")

strike = float(input("Enter strike: "))
strike_c_or_p = int(input("Enter (1) for CALLS, (2) for PUTS: "))

print("----------------------")