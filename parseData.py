

import numpy as np
import pandas as pd


import getDate





url='https://www.england.nhs.uk/statistics/wp-content/uploads/sites/2/2020/04/COVID-19-total-announced-deaths-' + getDate.getDateExcel() + '.xlsx'
print(url)

#url='https://www.england.nhs.uk/statistics/wp-content/uploads/sites/2/2020/04/COVID-19-total-announced-deaths-8-April-2020.xlsx'
df=pd.read_excel(url, sheet_name=1, skiprows=15)

#print(df.head())
#print(df)
#print(df.dropna(axis='columns', how='all').dropna(axis='rows', how='all'))

#cols=[c for c in df.columns if c.lower()[:] != 'Unnamed']
#df=df[cols]

df=df[df.columns.drop(list(df.filter(regex='Unnamed')))]
df=df[df.columns.drop(list(df.filter(regex='Awaiting verification')))]
df=df[df.columns.drop(list(df.filter(regex='Total')))]

dft=df.transpose()
dft.to_csv('./covid-19-totals-england-regions.csv')







