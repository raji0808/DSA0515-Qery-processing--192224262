import pandas as pd
data = {
    'Item': ['Item A', 'Item B', 'Item A', 'Item C'],
    'Date': ['2023-11-15', '2023-11-15', '2023-11-16', '2023-11-16'],
    'Units Sold': [30, 50, 20, 40]
}
sales_data = pd.DataFrame(data)
pivot_table = pd.pivot_table(sales_data, 
                             values='Units Sold', 
                             index='Item', 
                             aggfunc='sum')
print(pivot_table)
