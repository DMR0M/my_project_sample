import pandas as pd


ess = pd.read_csv('ess.csv')
print(ess.shape)
print(ess.loc[:, 'sclmeet'].head())
