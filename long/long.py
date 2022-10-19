import sys, os
dn=os.path.dirname(__file__)
pdn=os.path.join(dn,"..")
sys.path.append(pdn)
import utils
from Bio import SeqIO

inFile = sys.argv[1]

data=[]
for record in SeqIO.parse(inFile, 'fasta'):
    data.append(str(record.seq))

output=utils.shortest_superstring(data)
print(output)

