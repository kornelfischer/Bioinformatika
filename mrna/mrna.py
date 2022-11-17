import sys, os
dn=os.path.dirname(__file__)
pdn=os.path.join(dn,"..")
sys.path.append(pdn)
import utils

inFile = sys.argv[1]


def mrna(my_file="test.txt"):
    open_file = open(inFile, "r")
    data = open_file.read()
    table=utils.codon_table
    data=list(data[:-1])
    print(data)
    i=3
    for element in data:
        value = {key for key in table if table[key]==element}
        i *= len(value)
        i = i % 1_000_000
    print(i)

mrna(inFile)