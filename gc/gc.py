#ID: gc
import sys
import numpy as np

inFile = sys.argv[1]

id_array=[]
gc_array=[]

def gc(my_file="test.txt"):
    open_file = open(inFile, "r")
    data = open_file.read()
    genes = data.split(">")[1:]
    for seq in genes:
        parts=seq.split("\n")
        seq_name = parts[0]
        seq = ''.join(parts[1:])
        seq_gc = float(100*((seq.count('G')+seq.count('C'))/len(seq)))
        id_array.append(seq_name)
        gc_array.append(seq_gc)
    j = np.argmax(gc_array)
    print(id_array[j])
    print(gc_array[j])
gc((input))