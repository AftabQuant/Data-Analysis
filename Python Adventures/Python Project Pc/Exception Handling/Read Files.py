data = open('data.txt', 'r+')
print(data.read())

data.write('\nModified by using python.')
print(data.read())