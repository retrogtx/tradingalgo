from dhanhq import dhanhq

dhan = dhanhq("1101799004","eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpc3MiOiJkaGFuIiwicGFydG5lcklkIjoiIiwiZXhwIjoxNzA3MTkzODk1LCJ0b2tlbkNvbnN1bWVyVHlwZSI6IlNFTEYiLCJ3ZWJob29rVXJsIjoiIiwiZGhhbkNsaWVudElkIjoiMTEwMTc5OTAwNCJ9.ssSMF0-CPJ2_SQ-ejib-0qqhy-z7bQEXH3Wh6UcH8OLwi99bP0WX31DR97k-rXUyNmF7I9qekjbRgeC1BSoAgg")

dhan.place_order(data)

dhan.place_order(
    tag='',
    transaction_type=dhan.BUY,
    exchange_segment=dhan.NSE,
    product_type=dhan.INTRA,
    order_type=dhan.MARKET,
    validity='DAY',
    security_id='1333',
    quantity=10,
    disclosed_quantity=0,
    price=0,
    trigger_price=0,
    after_market_order=False,
    amo_time='OPEN',
    bo_profit_value=0,
    bo_stop_loss_Value=0,
    drv_expiry_date=None,
    drv_options_type=None,
    drv_strike_price=None    
)