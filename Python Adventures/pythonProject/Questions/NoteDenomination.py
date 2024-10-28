amount = int(input("Enter The Amount : "))

denomination = [2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
count = [0] * len(denomination)

for i in range(len(denomination)):
    count[i] = amount // denomination[i]
    amount %= denomination[i]

for i in range(len(count)):
    if count[i] > 0:
        print(denomination[i]," -> ", count[i])
