import sys

if len(sys.argv) < 2:
    print("Should be at least input argument")
    exit(12)

print(sys.argv[1:len(sys.argv)])
# input_val = sys.argv[1]
# print([x.strip() for x in input_val.split(',')])
