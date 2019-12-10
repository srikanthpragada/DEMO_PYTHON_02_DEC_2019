def sum_of_digits(n):
    return sum(map(int, str(n)))


nums = [2344, 3333, 11121, 2232, 332, 4344]

for n in filter(lambda n: sum_of_digits(n) > 10, nums):
    print(n)

for n in map(sum_of_digits, nums):
    print(n)
