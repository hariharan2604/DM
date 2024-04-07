#Hariharan J
#21BIT0143
import pandas as pd
df = pd.read_csv('after_binning.csv')

columns_to_normalize = ['Weekly_Sales','Temperature','Fuel_Price']  

for column in columns_to_normalize:
    min_val = df[column].min()
    max_val = df[column].max()
    df[column] = (df[column] - min_val) / (max_val - min_val)

df.to_csv('normalized.csv', index=False)
