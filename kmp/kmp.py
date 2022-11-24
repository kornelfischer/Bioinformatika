import sys, os
from Bio import SeqIO

inFile = sys.argv[1]

for record in SeqIO.parse(inFile, 'fasta'):
    dna_str=str(record.seq)

def failure_array_computing(dna_str):
    failure_array=[0]*len(dna_str)
    prefix_length=0
    i=1
    while i < len(dna_str):
        if dna_str[i] == dna_str[prefix_length]:
            prefix_length += 1
            failure_array[i] = prefix_length
            i += 1
        else:
            if prefix_length != 0:
                prefix_length = failure_array[prefix_length-1]
            else:
                failure_array[i] = 0
                i += 1
    print(*failure_array)


failure_array_computing(dna_str)
