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