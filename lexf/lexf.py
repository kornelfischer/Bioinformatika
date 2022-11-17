import sys
from itertools import product
import math

inFile = sys.argv[1]

with open(inFile,"r") as file:
    for idx,line in enumerate(file):
        if idx==0:
            alphabet=line.split()
        else:
            length=int(line)  

perm=product(alphabet,repeat=length)
for i in list(perm):
    print(''.join(i))
