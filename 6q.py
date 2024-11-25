import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
np.random.seed(42)  
date_range = pd.date_range(start="2023-01-01", end="2023-12-31", freq="B")  
prices = np.random.uniform(low=80, high=150, size=len(date_range))  
volume = np.random.randint(low=100000, high=5000000, size=len(date_range))
data = {"Date": date_range, "Close": prices, "Volume": volume}
df = pd.DataFrame(data)
start_date = "2023-06-01"
end_date = "2023-09-30"
filtered_data = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)]
plt.figure(figsize=(12, 6))
plt.scatter(filtered_data['Volume'], filtered_data['Close'], color='blue', alpha=0.6)
plt.title("Alphabet Inc. Trading Volume vs. Stock Prices (Simulated Data)")
plt.xlabel("Trading Volume")
plt.ylabel("Close Price (USD)")
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
