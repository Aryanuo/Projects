import pandas as pd
import numpy as np

data = pd.DataFrame({
    'Color': ['AIMS','UAS','ALTAIR','AIMS','AIMS','UAS']
})

def one_hot_encode(column):
    unique_vals = sorted(column.unique())
    encoded = pd.DataFrame()
    for val in unique_vals:
        encoded[val] = (column == val).astype(int)
    return encoded

encoded_colors = one_hot_encode(data['Color'])
data = pd.concat([data, encoded_colors], axis=1)
print(data)