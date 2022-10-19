import sys

inFile = sys.argv[1]
count = 1

with open(inFile,"r") as f:
    for line in f:
        if count % 2 == 0:
          line=line.strip("\n")
          print(line)
        count += 1

#pelda futtatas: python file_reading.py rosalind_5.txt