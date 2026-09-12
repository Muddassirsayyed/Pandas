import pandas as pd

# DataFrame = A tabular data structure with rows and columns. (2 Dimensional) Similar to an Excel spreadsheet

data = {
    "Name": ["Spongebob", "Patrick", "Squidward"],
    "Age": [30, 35, 50]    
}

df = pd.DataFrame(data, index=["Employee 1", "Employee 2", "Employee 3"])


print(df.loc["Employee 2"])
print(df.loc["Employee 3"])
print(df.loc["Employee 1"])


print(df.iloc[2]) # this is used to print only the specific row


# How to add new column
df["Job"] = ["Cook", "N/A", "Cashier"]

print(df)

# how to add a new row
new_row = pd.DataFrame([
    {"Name": "Sandy", "Age": 28, "Job": "Engineer"},
    {"Name": "Eugene", "Age": 60, "Job": "Manager"}], index=["Employee 4", "Employee 5"]) 
# how many rows you want create that much dictionaries

# | this is a sepreate dataframe so we have yo merge it into a main dataframe.
# so we have to concatinate it 

df = pd.concat([df, new_row])

print(df)