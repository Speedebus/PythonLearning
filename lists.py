import random
highest = 0
list = [random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100)]
for x in range(5):
    if list[x] > highest:
        highest = list[x]
print(highest)
