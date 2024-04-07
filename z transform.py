import pandas as pd
df = pd.read_csv('after_binning.csv')

columns_to_normalize = ['Weekly_Sales','Temperature','Fuel_Price']
print(df)
for column in columns_to_normalize:
    mean_val = df[column].mean()
    std = df[column].std()
    df[column] = (df[column] - mean_val) / std

df.to_csv('normalized_z-transform.csv',index=False)