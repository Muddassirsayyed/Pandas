import pandas as pd

calories = {"Day 1": 1750, "Day 2": 2100, "Day 3": 1700}

series = pd.Series(calories)

print(series)

series.loc["Day 2"] += 500

print(series.loc["Day 2"])
print(series.loc["Day 3"])

print(series[series >= 2000])
print(series[series < 2000])