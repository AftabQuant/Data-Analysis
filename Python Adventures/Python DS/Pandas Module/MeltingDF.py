import  pandas as pd

data = {
    "Fruit" : ["Apple", "Mango", "Banana", "Cherry"],
    "Gender" : ["F", "M", "F", "M"],
    "Quantity" : [15, 10, 10, 3]
}
df = pd.DataFrame(data)

print(pd.melt(df,id_vars=["Fruit"],value_vars=["Gender", "Quantity"]))