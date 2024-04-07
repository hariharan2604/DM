import pandas as pd
df = pd.read_csv('after_binning.csv')

columns_to_normalize = ['Weekly_Sales','Temperature','Fuel_Price']

for column in columns_to_normalize:
    mean_val = df[column].mean()
    std_val = df[column].std()
    df[column] = (df[column] - mean_val) / std_val

df.to_csv('normalized.csv',index=False)