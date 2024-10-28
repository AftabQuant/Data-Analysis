string = input("Enter A String : ")
vowels = "aeiouAEIOU"
count = sum(1 for char in string if char in vowels)
print(count)