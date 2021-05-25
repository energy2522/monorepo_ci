import sys

if len(sys.argv) < 2:
    print("Should be at least input argument")
    exit(12)

input_val = sys.argv[1]
print([x.strip() for x in input_val.split(',')])
