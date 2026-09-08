import pandas as pd
# default labels are 1   2  3
# to change that numbering to   a    b    c
data = [100, 102, 104, 160, 202]

series = pd.Series(data, index=["a", "b", "c", "d", "e"])
# series = pd.Series(data, index=["apartment1", "Apertment2", "apartment3"])

# print(series.loc["c"]) = 200 # loc means Location by label

series.loc["c"] = 200
print(series)

print(series.iloc[2])

print(series [series >= 200])
print(series [series < 200])