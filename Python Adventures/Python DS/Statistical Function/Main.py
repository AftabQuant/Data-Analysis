import numpy as np
import statistics as stats

break_food = np.array([200, 300, 150, 130, 200, 280, 170, 188])

print(np.mean(break_food))

print(np.median(break_food))

print(stats.mode(break_food))

# Standard deviation
print(np.std(break_food))

# Variance
print(np.var(break_food))

# Corelation Coefficient 
price = [300, 100, 350, 150, 200]
sales = [10, 20, 7,17, 8]
print(np.corrcoef([price, sales]))
