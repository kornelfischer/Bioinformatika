import sys, os
import numpy as np
import pandas as pd
#nem a grafos megoldas

inFile = sys.argv[1]

def graph(my_file="test.txt"):
    #elmented a id-ket
    id_array=[]
    #elmented a seq-eket
    seq_array=[]
    open_file = open(inFile, "r")
    data = open_file.read()
    genes = data.split(">")[1:]
    for seq in genes:
        parts=seq.split("\n")
        seq_name = parts[0]
        seq = ''.join(parts[1:])
        id_array.append(seq_name)
        seq_array.append(seq)
    #elmented kulon a prefixeket es a suffixeket
    prefixes=[]
    suffixes=[]
    for seq in seq_array:
        prefix=seq[0:3]
        suffix=seq[-3:]
        prefixes.append(prefix)
        suffixes.append(suffix)
    #df-be rakod oket
    df = pd.DataFrame({'Id':id_array, 'Seq':seq_array, 'prefix':prefixes, 'suffix':suffixes})
    output=[]
    for i in range(df.shape[0]):
        #vegigiteralsz, keresed az egyezeseket
        tmp=df["suffix"][i]
        tmp_id=df["Id"][i]
        for j in range(df.shape[0]):
            if tmp==df["prefix"][j] and i!=j:
                output.append([tmp_id, df["Id"][j]])
    #kiirod a lista elemeit, vesszo nelkul, kulonbozo sorokba
    for elements in output:
        print(*elements)


graph(inFile)
