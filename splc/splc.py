import sys, os
dn=os.path.dirname(__file__)
pdn=os.path.join(dn,"..")
sys.path.append(pdn)
import utils
from Bio import SeqIO

inFile = sys.argv[1]

dnas=[]
for record in SeqIO.parse(inFile, 'fasta'):
    dnas.append(str(record.seq))

dna_str=dnas[0]
introns=dnas[1:]

for element in introns:
    dna_str=dna_str.replace(element,'')

rna_str=utils.RNA(dna_str)
prot_str=utils.prot(rna_str)
print(prot_str)