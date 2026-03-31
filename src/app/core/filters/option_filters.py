# ---- Filters user preferences ----
import pandas as pd

# print out data frame to string
def print_options(options_df, ticker):
    if "calls" in options_df:
        print(f"-----{ticker} CALLS-----")
        print(options_df["calls"].to_string())
    if "puts" in options_df:
        print(f"-----{ticker} PUTS-----")
        print(options_df["puts"].to_string())

# Filter/show how many strikes the user wants to view
def get_nearby_strikes(options_df, current_price, below=5, above=5):
    options_df = options_df.sort_values("strike").reset_index(drop=True)
    options_df["distance"] = abs(options_df["strike"] - current_price)

    atm_pos = options_df["distance"].idxmin()

    start = max(0, atm_pos - below)
    end = min(len(options_df), atm_pos + above + 1 )

    return options_df.iloc[start:end].drop(columns=["distance"])


def filter_volume(dataframe, volume):
    dataframe = dataframe.copy()  # avoid modifying the original
    dataframe["volume"] = pd.to_numeric(dataframe["volume"], errors='coerce').fillna(0)
    filtered_vol_df = dataframe[dataframe["volume"] >= volume]
    return filtered_vol_df

def open_int(dataframe, open_interest):
    dataframe = dataframe.copy()  # avoid modifying the original
    dataframe["openInterest"] = pd.to_numeric(dataframe["openInterest"], errors='coerce').fillna(0)
    filtered_open_int_df = dataframe[dataframe["openInterest"] >= open_interest]
    return filtered_open_int_df

def apply_filters():
    pass
