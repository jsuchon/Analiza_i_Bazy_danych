#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 14:21:03 2021

@author: jaroslaw
"""
from os.path import dirname, abspath
import pandas as pd

path_to_original_data = f'{dirname(dirname(abspath(__file__)))}/Original_Data/tb.csv'
path_to_result_data = f'{dirname(dirname(abspath(__file__)))}/Analysis_Data/result_tb.csv'

df = pd.read_csv(path_to_original_data)
print("Struktura oryginalnych danych:")
print(df)


df = pd.melt(df, id_vars=['iso2', 'year'], value_vars=list(df.columns)[2:],
             var_name='column', value_name='cases')

df['sex'] = df['column'].str[7]
df['age'] = df['column'].str[8:].map({
    '014': '0-14',
    '1524': '15-24',
    '2534': '25-34',
    '3544': '35-44',
    '4554': '45-54',
    '5564': '55-64',
    '65': '65+',
    'u': 'unknown'
})
df = df[~df['cases'].isnull()]
df = df[~df['age'].isnull()]
df = df[~df['iso2'].isnull()]
df['cases'] = df['cases'].astype(int)

df.rename(columns={'iso2': 'country'}, inplace=True)
df = df[['country', 'year', 'sex', 'age', 'cases']]
df = df.sort_values(["country", "year", "sex", "age"], ascending=True)
df = df.reset_index(drop=True)
df.to_csv(path_to_result_data, index=False)
print("Struktura przetworzonych danych:")
print(df)