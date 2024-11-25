import pandas as pd
data = {
    'School_Code': ['A', 'B', 'A', 'B', 'A'],
    'Class': [1, 2, 1, 2, 1],
    'Age': [12, 15, 11, 14, 13]
}
df = pd.DataFrame(data)
print("Shape:", df.shape)
print("Columns:", df.columns.tolist())
