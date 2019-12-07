enums = []
onums = []

while True:
    n = int(input("Enter a number [0 top stop] :"))
    if n == 0:
        break

    if n % 2 == 0:
        enums.append(n)
    else:
        onums.append(n)

for n in onums + enums:
    print(n)
