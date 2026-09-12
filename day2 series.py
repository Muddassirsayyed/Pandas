import pandas as pd

# series = A Pandas labeled array that can hold any type 
# Think of it like a single column in a spreadsheet (1-Dimensional)


data = [100, 102, 104]

series = pd.Series(data) # Series is a constructer not a function. The S is capital in series so it is a Constructor

print(series)

Float_data = [100.1, 102.2, 104.3]
series1 = pd.Series(Float_data)

print(series1)

str_data = ["Muddassir", "Mushtaque", "Sayyed"]
series2 = pd.Series(str_data)

print(series2)


bool_data = [True, False, True]
series3 = pd.Series(bool_data)

print(series3)