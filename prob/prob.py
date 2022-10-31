#ID: HAMM
import sys, os
dn=os.path.dirname(__file__)
pdn=os.path.join(dn,"..")
sys.path.append(pdn)
import utils
import math

inFile = sys.argv[1]

def prob(my_file="test.txt"):
    open_file=open(inFile,"r")
    data = open_file.read()
    data=data.strip("\n")
    data=data.replace('\n', ' ').split(" ")
    dna=data[0]
    finals=[]
    for probs in data[1:]:
        probs=float(probs)
        conv_dict={}
        conv_dict['G'],conv_dict['C']= probs/2,probs/2
        conv_dict['A'],conv_dict['T']= (1-probs)/2,(1-probs)/2
        dna_probs=list((lambda x: conv_dict.get(x))(i) for i in dna) 
        final=0
        for i in dna_probs:
           final += math.log(i,10)
        finals.append(final)
    print(*finals)

prob(inFile)