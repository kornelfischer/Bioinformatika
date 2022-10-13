#ID: REVC
import sys

inFile = sys.argv[1]

def complementing_a_strand_of_dna(my_file="test.txt"):
    open_file = open(inFile, "r")
    data = open_file.read()
    reverse=data[::-1]
    output=""
    for s in reverse:
        if s == 'A':
            output += "T"
        elif s =='C':
            output += "G"
        elif s =='G':
            output += "C"
        elif s =='T':
            output += "A"

    print(output)

complementing_a_strand_of_dna((input))