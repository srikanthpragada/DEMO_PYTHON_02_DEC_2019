import sys
import os

if len(sys.argv) < 2:
    print("Usage : python search_files pattern [startdir]")
    sys.exit(0)


if len(sys.argv) > 2:
    startdir = sys.argv[2]
else:
    startdir = "."

searchstring = sys.argv[1]

for name, dirs, files in os.walk(startdir):
    for f in files:
        if searchstring in f:
            print(name + f)