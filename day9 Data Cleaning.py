import pandas as pd 

'''
Data Cleaning = The process of fixing/removing:
                incomplete, incorrect, or irrelevant data.
                ~75% of work done with Pandas is data cleaning
'''

df = pd.read_csv("data.csv")

 
# 1. Drop irrelevant columns 
# how to remove whole column
# df = df.drop(columns=["Legendary", "No"])
# print(df)

# 2. How To handle Missing Data 


# df = df.dropna(subset=["Type2"])    # it means drop not available

# how to replace any missing values
# df = df.fillna({"Type2": "None"})

# print(df.to_string())


# 3. Fix inconsistance value
# df["Type1"] = df["Type1"].replace({"Grass": "GRASS",
#                                    "Fire": "FIRE", 
#                                    "Water": "WATER"})
# print(df.to_string())

# 4. Standardize text
# df["Name"] = df["Name"].str.lower()
# print(df.to_string())

# 5. Fix data types

# df["Legendary"] = df["Legendary"].astype(bool)
# print(df.to_string())


# 6.remove duplicate values
df = df.drop_duplicates()

print(df.to_string())
