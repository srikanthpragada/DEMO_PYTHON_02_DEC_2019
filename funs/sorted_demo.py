nums = [11, -20, 14, -55, 66, 89]

for n in sorted(nums, key=abs):
    print(n)

for n in sorted(nums, key=lambda v: v % 10):
    print(n)
