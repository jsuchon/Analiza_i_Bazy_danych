# -*- coding: utf-8 -*-
"""
Autor: Jaroslaw Suchon
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Zadanie 3 
def fun(x):
    return x**2+5

def plot_fun(min_val, max_val, fun, n=100):
    X = np.linspace(min_val, max_val, n)
    Y = fun(X)    
    plt.plot(X,Y)
    plt.ylabel('[Y]')
    plt.xlabel('[X]')
    plt.suptitle(f"Wykres w zakresie od {min_val} do {max_val}")
    plt.show()
    
plot_fun(-1, 1, fun)
plot_fun(-6, 6, fun)
plot_fun(0, 5, fun)

# Zadanie 4
df = pd.DataFrame(columns=['name', 'surname', 'age', 'sex'])

for i in range(5):
     df.loc[i] = [f'name{i}'] + [f'surname{i}'] + [i] +  ["M" if i%2==0 else "F"]

print("____________DataFrame.info()__________")
df.info() 
print("____________DataFrame.describe()__________")
print(df.describe())
print("____________DataFrame.head()__________")
print(df.head(n=3))