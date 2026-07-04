import pprint
import yfinance as yf

ticker = yf.Ticker("AAPL")

news = ticker.news

print(f"Articles found: {len(news)}")
print()

pprint.pp(news[0])