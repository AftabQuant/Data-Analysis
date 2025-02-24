result = lambda x, y : x*y

print(result(2,6))

res2 = lambda x: x**2
print(res2(3))
print(res2(25))

res3 = lambda nums: [print(i, end=" ") for i in nums]

(res3([1,2,3,4,5]))

def test4(nums):
    for i in range(len(nums)):
        nums[i] +=2
    return nums

print(test4([1,2,3,4,5]))
