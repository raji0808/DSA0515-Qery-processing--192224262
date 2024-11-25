import pandas as pd
import matplotlib.pyplot as plt
data = {
    "Date": ["10-03-16", "10-04-16", "10-05-16", "10-06-16", "10-07-16"],
    "Open": [774.25, 776.03, 779.31, 779.00, 779.66],
    "Close": [772.56, 776.43, 776.47, 776.86, 775.08],
}
df = pd.DataFrame(data)
df["Date"] = pd.to_datetime(df["Date"])
plt.plot(df["Date"], df["Open"], label="Open")
plt.plot(df["Date"], df["Close"], label="Close")
plt.xlabel("Date")
plt.ylabel("Price")
plt.title("Alphabet Inc. Stock Prices")
plt.legend()
plt.show()
