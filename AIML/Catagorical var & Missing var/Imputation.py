import pandas as pd
import numpy as np

choose = input("Enter your choice Mean,Median and Mode ")
data = pd.DataFrame({
    'Age': [25, np.nan, 30, 22, np.nan, 28],
    'Gender': ['Male', 'Female', np.nan, 'Female', 'Male', np.nan]
})
def impute_mean(column):
    mean_val = column.dropna().mean()
    return column.fillna(mean_val)

def impute_mode(column):
    mode_val = column.dropna().mode()
    return column.fillna(mode_val)

def impute_median(column):
    median_val = column.dropna().median()
    return column.fillna(median_val)

if(choose=="Mean"):
    data['Age_mean'] = impute_mean(data['Age'])

elif(choose=="Median"):
    data['Age_median'] = impute_median(data['Age'])

elif(choose=="Mode"):
    data['Age_mode'] = impute_mode(data['Age'])

print(data)
