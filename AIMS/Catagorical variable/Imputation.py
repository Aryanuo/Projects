import pandas as pd
import numpy as np

data = pd.DataFrame({
    'Age': [25, np.nan, 30, 22, np.nan, 28],
    'Gender': ['Male', 'Female', np.nan, 'Female', 'Male', np.nan]
})
def impute_mean(column):
    mean_val = column.dropna().mean()
    return column.fillna(mean_val)

data['Age_mean'] = impute_mean(data['Age'])

print(data)
