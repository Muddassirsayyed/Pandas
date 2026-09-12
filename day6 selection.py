import pandas as pd

df = pd.read_csv("data.csv", index_col="Name")



# SELECTION BY COLUMN
# print(df["Name"].to_string())
# print(df["Height"].to_string())
# print(df["Weight"].to_string())


# print(df[["Name","Height", "Weight"]].to_string())
# print(df.to_string())



# SELECTION BY ROW/s
# print(df.loc[0])
# print(df.loc[1])


#  How to search a specific data
# print(df.loc["Pikachu"])
print(df.loc["Charizard"])


# if we don't want  all the data so we use this 
# print(df.loc["Charizard":"Blastoise", ["Height", "Weight"]])

# integer based indexing
# print(df.iloc[0:11:2, 0:3])

