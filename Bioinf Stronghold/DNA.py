#ID: DNA
import sys

inFile = sys.argv[1]

def DNA(my_file="test.txt"):
    A=C=G=T = 0
    open_file = open(inFile, "r")
    data = open_file.read()
    for s in data:
        if s == 'A':
            A +=1
        elif s =='C':
            C +=1
        elif s =='G':
            G +=1
        elif s =='T':
            T +=1
        else:
            continue

    print(f"{A} {C} {G} {T}")

DNA((input))

#pelda futtatas: python DNA.py rosalind_dna.txt

