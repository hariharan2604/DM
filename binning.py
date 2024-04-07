#Hariharan J
#21BIT0143
import pandas as pd
df = pd.read_csv('missing.csv')

bin_edges = [0,1,10]
bin_labels = ['No Holiday','Holiday']

df['Binned_Column'] = pd.cut(df['Holiday_Flag'], bins=bin_edges, labels=bin_labels)

df.to_csv('after_binning.csv', index=False)
