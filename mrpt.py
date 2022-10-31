#id: mrpt
import sys
import requests

inFile = sys.argv[1]

def mrpt(my_file="test.txt"):
    open_file = open(inFile, "r")
    data = open_file.read()
    data=data.split("\n")
    ids=[]
    for seq in data:
        seq=seq.split("_")
        seq=seq[0]
        ids.append(seq)
    #print(ids)
    for i in range(len(ids)):
        resp=requests.get("http://www.uniprot.org/uniprot/"+ids[i]+".fasta")
        prot_seq=resp.text
        print(prot_seq)

    



mrpt(inFile)