import pandas as pd
# pandas is represented as panel data

# we can work in pandas with series (its like a single data columnb 1D Column) and Dataframe (its like a full data table 2D column)
df = pd.read_csv("data.csv")

# Filtering = keeping the rows that match a condition

# tall_pokemon = df[df["Height"] >= 2]
heavy_pokemon = df[df["Weight"] > 100]

print(heavy_pokemon)