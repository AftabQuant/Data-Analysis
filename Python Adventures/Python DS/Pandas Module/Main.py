import pandas as pd

# Create a DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)

# Display the DataFrame
print(df)

# Calculate the mean age
mean_age = df['Age'].mean()
print(f'Mean Age: {mean_age}')
