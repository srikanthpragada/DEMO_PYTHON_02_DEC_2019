
squares = []

for n in range(1,11):
    squares.append(n * n)

print(squares)

sqrs = [n * n for n in range(1,30) if n % 3 == 0 or n % 5 == 0]
print(sqrs)
