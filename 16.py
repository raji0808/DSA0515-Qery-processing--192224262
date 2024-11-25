import pandas as pd
data = {
    'School_Code': ['A', 'B', 'A', 'B', 'A'],
    'Name': ['Tom', 'Jerry', 'Anna', 'Mike', 'Sara'],
    'Age': [12, 15, 11, 14, 13]
}
df = pd.DataFrame(data)
grouped = df.groupby('School_Code')
print(type(grouped))


