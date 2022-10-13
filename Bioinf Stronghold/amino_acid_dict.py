#ID: PROT
import sys

inFile = sys.argv[1]

codon_table ={
	'UUU': 'F',
	'CUU': 'L',
	'AUU': 'I',
	'GUU': 'V',
	'UUC': 'F',
	'CUC': 'L',
	'AUC': 'I',
	'GUC': 'V',
	'UUA': 'L',     
	'CUA': 'L',     
	'AUA': 'I',     
	'GUA': 'V',
	'UUG': 'L',     
	'CUG': 'L',     
	'AUG': 'M',     
	'GUG': 'V',
	'UCU': 'S',     
	'CCU': 'P',     
	'ACU': 'T',     
	'GCU': 'A',
	'UCC': 'S',     
	'CCC': 'P',     
	'ACC': 'T',     
	'GCC': 'A',
	'UCA': 'S',    
	'CCA': 'P',     
	'ACA': 'T',     
	'GCA': 'A',
	'UCG': 'S',     
	'CCG': 'P',     
	'ACG': 'T',     
	'GCG': 'A',
	'UAU': 'Y',     
	'CAU': 'H',     
	'AAU': 'N',     
	'GAU': 'D',
	'UAC': 'Y',     
	'CAC': 'H',     
	'AAC': 'N',     
	'GAC': 'D',
	'UAA': 'Stop',
	'CAA': 'Q',      
	'AAA': 'K',      
	'GAA': 'E',
	'UAG': 'Stop',
	'CAG': 'Q',      
	'AAG': 'K',      
	'GAG': 'E',
	'UGU': 'C',      
	'CGU': 'R',      
	'AGU': 'S',      
	'GGU': 'G',
	'UGC': 'C',      
	'CGC': 'R',      
	'AGC': 'S',      
	'GGC': 'G',
	'UGA': 'Stop',
	'CGA': 'R',      
	'AGA': 'R',      
	'GGA': 'G',
	'UGG': 'W',
	'CGG': 'R',
	'AGG': 'R',      
	'GGG': 'G'
}

def amino_acid_dict(my_file="test.txt"):
	open_file=open(inFile,"r")
	data = open_file.read()
	data=data.strip("\n")
	output=""
	for i in range(0,len(data),3):
		char=data[i:i+3]
		amino_acid=codon_table[char]
		if amino_acid=="Stop":
			continue
		output += amino_acid

	print(output)
amino_acid_dict((input))
