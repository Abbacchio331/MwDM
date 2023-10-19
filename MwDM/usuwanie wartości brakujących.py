import pandas as pd
import numpy as np

def space(n):
  for i in range(n):
    print(" ")

A = np.array([1, 2, 3, np.nan])
print("Przykładowa lista:\n", A)

space(1)

print("Jej typ:",  A.dtype)
print("Jej suma:", A.sum())
print("Jej średnia arytmetyczna:", A.mean())

space(1)

B = pd.Series([np.nan, None])
print("Przykładowy szereg:\n", B)

space (1)

print("Zastosowanie na nim funkcji isnull():\n", (B.isnull()))
print("Zastosowanie na nim funkcji notnull():\n", (B.notnull()))

space(1)

df = pd.DataFrame([[1, 2, 3],
[4,5,np.nan],
[np.nan,8,9]])
print("Przykładowa ramka danych:\n", df)

space(1)

print("Zastosowanie na niej funkcji dropna(axis=0):\n", df.dropna())
space(1)
print("Zastosowanie na niej funkcji dropna(axis=1):\n", df.dropna(axis=1))
space(1)


df1 = pd.DataFrame([[np.nan, 2, 3],
[np.nan,np.nan,6],
[np.nan,8,9]])
print("Kolejna przykładowa ramka danych:\n", df1)
space(1)

print('Zastosowanie na niej funkcji dropna(axis=1, how="any"):\n', df1.dropna(axis=1, how="any"))
space(1)
print('Zastosowanie na niej funkcji dropna(axis=1, how="all")):\n', df1.dropna(axis=1, how="all"))
space(1)
print('Zastosowanie na niej funkcji dropna(axis=0, thresh=2)):\n', df1.dropna(axis=0, thresh=2))
space(1)
