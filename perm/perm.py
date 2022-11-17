import sys
from itertools import permutations 
import math

inFile = sys.argv[1]
open_file = open(inFile, "r")
data = int(open_file.read()[0])
perm=permutations([i+1 for i in range(data)])
print(math.factorial(data))
for i in list(perm):
    print(*i)