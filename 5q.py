# Sample data for trading volumes
data_volume = {
    "Date": [
        "2024-01-01", "2024-01-02", "2024-01-03", "2024-01-04", "2024-01-05",
        "2024-01-06", "2024-01-07", "2024-01-08", "2024-01-09", "2024-01-10"
    ],
    "Trading Volume": [1200000, 1300000, 1250000, 1350000, 1400000, 1500000, 1450000, 1550000, 1600000, 1650000]
}

df_volume = pd.DataFrame(data_volume)
df_volume["Date"] = pd.to_datetime(df_volume["Date"])

# Filter data between two specific dates
start_date = "2024-01-03"
end_date = "2024-01-08"
filtered_volume_df = df_volume[(df_volume["Date"] >= start_date) & (df_volume["Date"] <= end_date)]

# Create the bar plot
plt.figure(figsize=(10, 6))
plt.bar(filtered_volume_df["Date"], filtered_volume_df["Trading Volume"], color="skyblue", label="Trading Volume")
plt.title("Alphabet Inc. Trading Volume", fontsize=16)
plt.xlabel("Date", fontsize=12)
plt.ylabel("Trading Volume", fontsize=12)
plt.grid(axis="y")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
