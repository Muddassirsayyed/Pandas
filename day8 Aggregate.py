import pandas as pd

# aggregate functions = Reduces a set of values into a single summary value
# Used to summarize and analyze data

# Often used with the groupby() function  

df = pd.read_csv("data.csv")


#  Whole Dataframe

# print(df.mean(numeric_only=True)) find the average of anything

# sum of all the numbers 
# print(df.sum(numeric_only=True))

# minimum of all the values
# print(df.min(numeric_only=True))


# # maximum of all the values
# print(df.max(numeric_only=True))

# print(df.count())



# Sigle column 

# print(df["Height"].mean()) # it is numeric so we dont have to pass the numeric argument 

# print(df["Height"].sum())
# print(df["Height"].min())
# print(df["Height"].max())
# print(df["Height"].count())



# how to use groupby() funtion
# for example we can group all the grass type in one group
group = df.groupby("Type1")

# print(group["Height"].mean())
# print(group["Height"].sum())
# print(group["Height"].min())
# print(group["Height"].max())
print(group["Height"].count())