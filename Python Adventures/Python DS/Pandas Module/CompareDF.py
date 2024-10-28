import  pandas as pd

data = {
    "Fruit" : ["Apple", "Mango", "Banana", "Cherry"],
    "Price" : [100, 150, 50, 35],
    "Quantity" : [15, 10, 10, 3]
}
df = pd.DataFrame(data)
print(df)
df2 = df.copy()
df2.loc[0, "Price"] = 120
df2.loc[1, "Price"] = 175
df2.loc[2, "Price"] = 100
df2.loc[0, "Quantity"] = 30
print(df2)
print()
print(df.compare(df2))



