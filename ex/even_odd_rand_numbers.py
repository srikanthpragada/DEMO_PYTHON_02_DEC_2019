import random

enums = []
onums = []

for i in range(1,11):
    n = random.randint(1,100)
    if n % 2 == 0:
        enums.append(n)
    else:
        onums.append(n)

for n in onums + enums:
    print(n)
