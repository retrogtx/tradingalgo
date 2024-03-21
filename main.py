import pandas as pd
from dhanhq import dhanhq

dhan = dhanhq("client_id","access_token")

data = dhan.historical_daily_data(
    symbol='TCS',
    exchange_segment='NSE_EQ',
    instrument_type='EQUITY',
    expiry_code=0,
    from_date='2022-01-08',
    to_date='2022-02-08'
)


def detect_cup_and_handle(data):
    data['Price Change'] = data['Close'].pct_change()
    start = data['Price Change'].idxmax()
    end = data['Price Change'].idxmin()
    data['Price Change'] = data['Close'].pct_change()
    start = data['Price Change'].idxmax()
    end = data['Price Change'].idxmin()
    data['Price Change'] = data['Close'].pct_change()
    start = data['Price Change'].idxmax()
    end = data['Price Change'].idxmin()
    if end - start < 10:
        return True
    else:
        return False