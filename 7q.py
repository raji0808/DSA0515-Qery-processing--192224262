import pandas as pd
data = {
    "Item": ["Item_A", "Item_B", "Item_C", "Item_A", "Item_B", "Item_C"],
    "Region": ["East", "West", "East", "North", "East", "South"],
    "Date": ["2023-01-01", "2023-01-02", "2023-01-03", "2023-01-04", "2023-01-05", "2023-01-06"],
    "Sales": [200, 340, 150, 500, 120, 250]
}
df = pd.DataFrame(data)
pivot_table = pd.pivot_table(df, values="Sales", index="Item", aggfunc=["max", "min"])
print("Pivot Table:")
print(pivot_table)
