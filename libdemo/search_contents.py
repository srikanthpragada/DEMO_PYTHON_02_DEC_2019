import sys
import os


def has_pattern(filename, pattern):
    with open(filename,"rt") as f:
        return pattern in f.read()


if len(sys.argv) < 2:
    print("Usage : python search_contents pattern [startdir]")
    sys.exit(0)


if len(sys.argv) > 2:
    startdir = sys.argv[2]
else:
    startdir = "."

searchstring = sys.argv[1]

for name, dirs, files in os.walk(startdir):
    for f in files:
        if f.endswith(".py"):
          filename = name + "\\" + f
          if has_pattern(filename, searchstring):
             print(filename)