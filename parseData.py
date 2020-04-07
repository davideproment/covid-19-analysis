

import numpy as np
import pandas as pd

url='https://www.england.nhs.uk/statistics/wp-content/uploads/sites/2/2020/04/COVID-19-total-announced-deaths-7-April-2020.xlsx'
df=pd.read_excel(url, sheet_name=1, skiprows=15)

#print(df.head())
#print(df)
#print(df.dropna(axis='columns', how='all').dropna(axis='rows', how='all'))

dft=df.transpose()
dft.to_csv('./covid-19-totals-england-regions.csv')







