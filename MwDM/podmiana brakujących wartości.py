import pandas as pd
import numpy as np


def space(n):
  for i in range(n):
    print(" ")

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