import pandas as pd
data = {'Names': ['Tom', 'Jerry', 'Anna', 'Mike', 'Sara']}
df = pd.DataFrame(data)
df['Substring_Index'] = df['Names'].str.find('An')
print(df)
