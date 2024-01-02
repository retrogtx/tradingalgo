from dhanhq import dhanhq

dhan = dhanhq("client_id", "access_token")
dhan.historical_minute_charts(data)

dhan.place_order(data)
