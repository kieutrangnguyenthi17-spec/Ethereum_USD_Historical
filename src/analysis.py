import pandas as pd
import matplotlib.pyplot as plt

# LOAD DATA

df = pd.read_csv("../data/ethereum_usd_historical_dataset.csv")

print("Columns:", df.columns)

df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values("Date")


# 1 PRICE TREND

plt.figure(figsize=(10,5))

plt.plot(df["Date"], df["Close"])

plt.title("Ethereum Price Trend")
plt.xlabel("Date")
plt.ylabel("Price (USD)")

plt.tight_layout()
plt.savefig("../images/price_trend.png")


# 2 MOVING AVERAGE

df["MA50"] = df["Close"].rolling(50).mean()
df["MA200"] = df["Close"].rolling(200).mean()

plt.figure(figsize=(10,5))

plt.plot(df["Date"], df["Close"], label="Close")
plt.plot(df["Date"], df["MA50"], label="MA50")
plt.plot(df["Date"], df["MA200"], label="MA200")

plt.title("Moving Average")
plt.xlabel("Date")
plt.ylabel("Price")

plt.legend()

plt.tight_layout()
plt.savefig("../images/moving_average.png")

# 3 VOLATILITY

df["Volatility"] = df["Close"].pct_change().rolling(30).std()

plt.figure(figsize=(10,5))

plt.plot(df["Date"], df["Volatility"])

plt.title("30-Day Volatility")
plt.xlabel("Date")
plt.ylabel("Volatility")

plt.tight_layout()
plt.savefig("../images/volatility.png")

# 4 RSI

delta = df["Close"].diff()

gain = delta.clip(lower=0)
loss = -delta.clip(upper=0)

avg_gain = gain.rolling(14).mean()
avg_loss = loss.rolling(14).mean()

rs = avg_gain / avg_loss

df["RSI"] = 100 - (100/(1+rs))

plt.figure(figsize=(10,5))

plt.plot(df["Date"], df["RSI"])

plt.axhline(70)
plt.axhline(30)

plt.title("RSI Indicator")
plt.xlabel("Date")
plt.ylabel("RSI")

plt.tight_layout()
plt.savefig("../images/rsi.png")

plt.show()

print("4 charts created successfully!")