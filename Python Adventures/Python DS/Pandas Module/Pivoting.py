import  pandas as pd

data = {
    "Fruit" : ["K1", "K2", "K1", "K2"],
    "Price" : [100, 150, 50, 35],
    "Quantity" : [15, 10, 10, 3]
}
df = pd.DataFrame(data)
print(df.pivot(index="Fruit", columns="Price", values="Quantity"))
