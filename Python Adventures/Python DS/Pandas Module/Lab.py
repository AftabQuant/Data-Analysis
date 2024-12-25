import pandas as pd
data = {
    "Fruit" : ["apple", "Mango", "Banana", "Cherry"],
    "Price" : [100, 150, 50, 35],
    "Quantity" : [15, 10, 10, 3],
    "Quantity1" : [15, 10, 10, 3]
}
df = pd.DataFrame(data)
df2 = df.drop('Quantity1', axis=1)
print(df2)

df.rename(columns = {'Quantity1': "Check"}, inplace= True)
print(df)

df3 = df2[['Price','Fruit','Quantity']]
print(df3)

array = df.to_numpy()
print(array)

df['Fruit'] = df['Fruit'].replace('a', 'A')
print(df)