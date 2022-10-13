#ID: RNA
import sys

inFile = sys.argv[1]

def RNA(my_file="test.txt"):
    open_file = open(inFile, "r")
    data = open_file.read()
    output=""
    for s in data:
        if s == 'T':
            output += "U"
        else:
            output += s

    print(output)

RNA((input))