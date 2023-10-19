import pandas as pd
import numpy as np


def space(n):
  for i in range(n):
    print(" ")


#Usuwanie duplikatów
print("---- Usuwanie duplikatów ----")

df = pd.DataFrame([["a", "2", "c"], [1, 2, 3], [4, "b", 6], [4, 5, 6],
                   ["a", "2", "c"], [4, 5, 6]])
print(df)
space(3)

df = df.drop_duplicates()

print(df)
space(6)

#Podmiana brakujących danych wartościami średnimi
print("---- Podmiana brakujących danych wartościami średnimi ----")
df_1 = pd.DataFrame([[1, 2, np.nan, 1, 2, 3], [4, 2, 6, np.nan, 5, 6]])
df_1 = df_1.T
print(df_1)
space(3)

for i in range(df_1.shape[1]):
  col_mean = np.mean(df_1.iloc[:, i])
  df_1.iloc[:, i].fillna(col_mean, inplace=True)

print(df_1)
space(6)

#Wykrywanie elementów nietypowych przy użyciu metody Hampela
print("---- Wykrywanie elementów nietypowych przy użyciu metody Hampela ----")

data = [1, 2, 6, 2, 7, 2, 5, 8, 1, 3, 99]

print(data)
space(3)

s = 1.4826 * np.median([abs(i - np.median(data)) for i in data])
print(f"Współczynnik skali MAD = {s}")
space(3)

for i in data:
  if abs(i - np.median(data)) > 3 * s:
    print(f"W podanym zbiorze danych {i} jest elementem odosobnionym.")
