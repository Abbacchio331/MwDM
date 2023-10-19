import pandas as pd
import numpy as np
import re


def space(n):
  for i in range(n):
    print(" ")


#Formatowanie danych
print("---- Formatowanie danych ----")
space(3)
print("Dane wejściowe:")
df = pd.DataFrame([["wysoki", "55kg", 9999], [180, "65kg", 10],
                   ["niski", 75, pd.NA]])
df.columns = ["wzrost", "waga", "iq"]
print(df)
space(3)
print("""Wartości które powinny się znaleźć w bazie:
wzrost: niski (do 140cm), średni (od 141cm do 170cm), wysoki (od 171cm)
waga: liczba całkowita
iq: liczba całkowita z zakresu 0-200

dane domyślne:
wzrost: <NA>
waga: <NA>
IQ: <NA>
""")

space(3)
print("Dane, które nie spełniają warunków w kolumnie wzrost:")
for i in df.index:
  if df.wzrost[i] not in ["niski", "średni", "wysoki"]:
    print(f"- osoba {i}, wzrost: {df.wzrost[i]}")
    if type(df.wzrost[i]) == int:
      if df.wzrost[i] < 141:
        df.wzrost[i] = "niski"
      elif df.wzrost[i] < 171:
        df.wzrost[i] = "średni"
      else:
        df.wzrost[i] = "wysoki"

space(3)
print("Dane, które nie spełniają warunków w kolumnie waga:")
for i in df.index:
  waga = df.waga[i]
  if type(waga) != int:
    print(f"- osoba {i}, waga: {df.waga[i]}")
    if re.match(r'^\d+kg$', waga):
      df['waga'][i] = int(re.search(r'\d+', waga).group())
    else:
      try:
        df['waga'][i] = int(waga)
      except ValueError:
        df['waga'][i] = pd.NA

space(3)
print("Dane, które nie spełniają warunków w kolumnie iq:")
for i in df.index:
  if type(df.iq[i]) != int or df.iq[i] < 0 or df.iq[i] > 200:
    print(f"- osoba {i}, wzrost: {df.iq[i]}")
    df.iq[i] = pd.NA

space(3)
print("Dane wyjściowe:")
print(df)
