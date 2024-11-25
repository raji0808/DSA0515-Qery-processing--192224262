import pandas as pd
data = {
    'School_Code': ['A', 'B', 'A', 'B', 'A'],
    'Class': [1, 2, 1, 2, 1],
    'Age': [12, 15, 11, 14, 13]
}
df = pd.DataFrame(data)
grouped = df.groupby(['School_Code', 'Class'])
for name, group in grouped:
    print(name)
    print(group)
