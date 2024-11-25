import pandas as pd
import matplotlib.pyplot as plt

# Sample data for historical stock prices
data = {
    "Date": [
        "2024-01-01", "2024-01-02", "2024-01-03", "2024-01-04", "2024-01-05",
        "2024-01-06", "2024-01-07", "2024-01-08", "2024-01-09", "2024-01-10"
    ],
    "Stock Price": [1500, 1520, 1510, 1530, 1550, 1540, 1560, 1580, 1570, 1590]
}

df = pd.DataFrame(data)
df["Date"] = pd.to_datetime(df["Date"])

# Filter data between two specific dates
start_date = "2024-01-03"
end_date = "2024-01-08"
filtered_df = df[(df["Date"] >= start_date) & (df["Date"] <= end_date)]

# Create the line plot
plt.figure(figsize=(10, 6))
plt.plot(filtered_df["Date"], filtered_df["Stock Price"], marker="o", label="Stock Price")
plt.title("Alphabet Inc. Historical Stock Prices", fontsize=16)
plt.xlabel("Date", fontsize=12)
plt.ylabel("Stock Price (USD)", fontsize=12)
plt.grid(True)
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
