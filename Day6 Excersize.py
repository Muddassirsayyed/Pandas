import pandas as pd

df = pd.read_csv("data.csv",index_col="Name")

pokemon = input("Enter the Pokemon Name: ")

try:
    print(df.loc[pokemon])

except KeyError:
    print(f"{pokemon} Not Found")