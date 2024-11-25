import pandas as pd
data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Profession': ['Engineer', 'Doctor', 'Artist']}
df = pd.DataFrame(data)
df['Profession'] = df['Profession'].str.swapcase()
print(df)
