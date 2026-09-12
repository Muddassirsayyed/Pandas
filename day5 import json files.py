import pandas as pd

df = pd.read_json("data.json")


# to_string() iss liye use hua Q ki direct df print karne par paheli 5 or last 5 rows show ho rahie thi 
# to_string ka use karne se full data show hota hai
print(df.to_string())