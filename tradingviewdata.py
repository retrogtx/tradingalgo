from tvDatafeed import TvDatafeed, Interval
tv = TvDatafeed()

data = tv.get_hist(symbol='NIFTY',exchange='NSE',interval=Interval.in_5_minute,n_bars=4000)

print(data)
data.to_csv('nifty50.csv')

