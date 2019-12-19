import os

for name, dirs, files in os.walk(r"e:\classroom\python\dec2"):
    for f in files:
        if 'demo' in f:
            print(name + f)
