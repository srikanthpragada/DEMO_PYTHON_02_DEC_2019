def iseven(n):
    return n % 2 == 0


nums = [11, 20, 14, 55, 66, 89]

for n in nums:
    if n % 2 == 0:
        print(n)

for n in filter(iseven, nums):
    print(n)

for n in filter(lambda n : n % 2 == 1, nums):
    print(n)

for n in filter(lambda s : len(s) > 3, ['Larry','Joe','Li','Steve']):
    print(n)
