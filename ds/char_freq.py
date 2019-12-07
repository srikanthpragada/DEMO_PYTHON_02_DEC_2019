st = "This is fine. Programming is fun"

freq = {}   # Empty dict
for c in st:
    if c in freq:
        freq[c] += 1    # Increment count
    else:
        freq[c] = 1     # Add a new key(char) with 1

print(freq)




