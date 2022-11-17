import sys

inFile = sys.argv[1]

open_file=open(inFile,"r")
n = int(open_file.read())
sset=2**n % 1_000_000
print(sset)