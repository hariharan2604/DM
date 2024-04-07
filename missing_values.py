#Hariharan J
#21BIT0143
import pandas as pd
df = pd.read_csv('walmart.csv')

df.fillna(0, inplace=True)

df.to_csv('missing.csv', index=False)
