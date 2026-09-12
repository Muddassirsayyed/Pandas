import pandas as pd

data = {
    "Name":["Muddassir", "Iram", "yash", "Aftab", "Hasnain", "Huzefa"],
    "Age": [20, 22, 21, 17, 23, 19]
}

df = pd.DataFrame(data, index=["Employee 1","Employee 2","Employee 3", "Employee 4", "Employee 5", "Employee 6"])

# adding new column Job

df["Job"] = ["Software Engineer", "software Developer", "Manager", "Web Developer", "FrontEnd Developer", "Backend Developer"]

print(df    )