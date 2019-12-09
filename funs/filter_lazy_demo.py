def iseven(n):
    print("Calling with ", n)
    return n % 2 == 0


nums = [11, 20, 14, 55, 66, 89]

# filter object is created and no selection is done
f = filter(iseven, nums)

for v in f:  # function iseven is called for each element
    print(v)
