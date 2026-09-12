import pandas as pd

df = pd.read_csv("data.csv")

# Filtering = keeping the rows that match a condition


'''
filtering example:
    Suppose we have to to filter the pokemon that have a hight more than or equals to 2 meter
'''
# tall_pokemon = df[df["Height"] >= 2]
# print(tall_pokemon)

# heavy_pokemon = df[df["Weight"] >= 100]
# print(heavy_pokemon)

# legendary_pokemon = df[df["Legendary"] > 0] # we can replace 1 with true here
# print(legendary_pokemon)


# how to find water pokemon

# water_pokemon = df[(df["Type1"] == "Water") | 
#                    (df["Type2"] == "Water")]
# print(water_pokemon)


# how to find fire and flying pokemon 

# fire_and_flying_pokemon = df[(df["Type1"] == "Fire") &
#                              (df["Type2"] == "Flying")]

# print(fire_and_flying_pokemon)

# how to find grass and water pokemon
grass_and_water_pokemon = df[(df["Type1"] == "Grass") |
                             (df["Type2"] == "Poision")]

print(grass_and_water_pokemon)