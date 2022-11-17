import sys
from itertools import product
from Bio import SeqIO

inFile = sys.argv[1]
for record in SeqIO.parse(inFile, 'fasta'):
    dna=(str(record.seq))
N=len(dna)
alphabet=['A','C','G','T']
kmer_dict=dict()
perm=product(alphabet,repeat=4)
for i in list(perm):
    kmer_dict[''.join(i)] = 0

for i in range(N-3):
    kmer=dna[i:i+4]
    kmer_dict[kmer] += 1

composition_list=list(kmer_dict.values())
print(*composition_list)