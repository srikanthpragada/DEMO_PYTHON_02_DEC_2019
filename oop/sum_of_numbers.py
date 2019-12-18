sum = 0
count = 0

while True:
    try:
        n = int(input("Enter a number [0 to stop] :"))
        if n == 0:
            break

        if n < 0:
            continue

        sum += n
        count += 1
    except:
       print("Invalid number!")

print("Average = ", sum / count)
