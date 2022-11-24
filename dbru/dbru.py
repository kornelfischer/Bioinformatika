import sys

inFile = sys.argv[1]

def revc(sequence):
    reverse=sequence[::-1]
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

    return(output)

with open(inFile,"r") as file:
    lines = map(str.strip, file.readlines())
    kmers=set()
    for line in lines:
        kmers.add((line[:-1], line[1:]))
        rc=revc(line)
        kmers.add((rc[:-1],rc[1:]))
    for (a,b) in sorted(kmers):
        print(f"({a}, {b})")