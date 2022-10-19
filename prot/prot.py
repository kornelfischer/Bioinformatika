#ID: PROT
import sys, os
dn=os.path.dirname(__file__)
pdn=os.path.join(dn,"..")
sys.path.append(pdn)
import utils

inFile = sys.argv[1]

def prot(my_file="test.txt"):
	open_file=open(inFile,"r")
	data = open_file.read()
	data=data.strip("\n")
	output=""
	for i in range(0,len(data),3):
		char=data[i:i+3]
		amino_acid=utils.codon_table[char]
		if amino_acid=="Stop":
			continue
		output += amino_acid

	print(output)
prot((input))
