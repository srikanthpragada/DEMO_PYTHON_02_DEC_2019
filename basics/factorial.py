# Factorial program

import sys

if len(sys.argv) < 2:
    print("Usage : python factorial.py number")
    sys.exit(0)

n = int(sys.argv[1])

fact = 1
for i in range(2, n + 1):
    fact = fact * i

print(f"Factorial of {n} is {fact}")
