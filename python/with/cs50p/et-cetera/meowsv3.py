import sys

if len(sys.argv) == 1:
    print("meow")
elif len(sys.argv) == 3 and (sys.argv[1] in ["-n", "--number"]):
    n = int(sys.argv[2].strip())
    for _ in range(n):
        print("meow")
else:
    print("usage: meowsv3.py [-n | --number] <number>")
