import sys, os
import numpy as np
import pandas as pd

inFile = sys.argv[1]

def gc(my_file="test.txt"):
    id_array=[]
    gc_array=[]
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

def graph(my_file,overlap):
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
        prefix=seq[0:overlap]
        suffix=seq[-overlap:]
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

    return(output)

def shortest_superstring(data_list,superstring=''):
    #esetek ellenorzese kell
    if len(data_list) == 0: #kifogytak a szekvenciak, vegeztunk
        return superstring
    
    elif len(superstring) == 0: #ez az elejen van, el kell kezdenunk az algoritmust valahogy
        superstring = data_list.pop(0) #bepakoljuk a legelsot, megyunk tovabb
        return shortest_superstring(data_list,superstring)
        
    else:
        length=len(data_list) # a szekvenciak darabszama
        for idx in range(length):   #vegigmegyunk rajtuk
            curr_seq=data_list[idx] #a mostani szekv
            curr_seq_len=len(curr_seq)  # amostani szekv hossza

            for i in range(curr_seq_len // 2):  #tudjuk, hogy legalabb felig fedik egymast, probalgatunk
                overlap_len = curr_seq_len - i

                if superstring.startswith(curr_seq[i:]): # ha a mostani superstring mar azzal kezdodik, mint amire vegzodik a mostanink, akkor bepakoljuk az elejere
                    data_list.pop(idx) #kiszedjuk a listabol, mert besoroltuk
                    return shortest_superstring(data_list,curr_seq[:i] + superstring) #rekurziv hivas

                if superstring.endswith(curr_seq[:overlap_len]): # ha a mostani superstring mar azzal vegzodik, mint amivel kezdodik a mostanink, akkor bepakoljuk a vegere
                    data_list.pop(idx) #kiszedjuk a listabol, mert besoroltuk
                    return shortest_superstring(data_list,superstring + curr_seq[overlap_len:]) #rekurziv hivas


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
