import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.rand(10, 4), columns=['A', 'B', 'C', 'D'])
df.loc[3, 'B'] = np.nan
df.loc[6, 'C'] = np.nan
def highlight_nan(s):
    return ['background-color: yellow' if pd.isna(v) else '' for v in s]
styled_df = df.style.apply(highlight_nan, axis=0)
styled_df
