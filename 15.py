import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.rand(10, 4), columns=['A', 'B', 'C', 'D'])
filtered_df = df[df.isnull().sum(axis=1) >= 2]
print(filtered_df)
