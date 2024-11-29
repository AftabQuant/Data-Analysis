add = lambda a,b : a+b
print(add(3,4))

a = {'apple' : 5, 'banana' : 2, 'cherry' : 2, 'date' : 1}
key = sorted(a.items())


sq = {x**2 for x in range(1,4)}
print(sq)

ar = [1,2,3,4,5,6,7,8,9,10]
even = list(filter(lambda x : x%2==0, ar))
print(even)