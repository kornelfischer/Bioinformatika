import sys, os
dn=os.path.dirname(__file__)
pdn=os.path.join(dn,"..")
sys.path.append(pdn)
import utils
import networkx as nx

inFile = sys.argv[1]
#beolvassuk a reszleteket
with open(inFile) as input_data:
    dna_str = [line.strip() for line in input_data.readlines()]

total_legth=sum(len(element) for element in dna_str)
longest=max(len(element) for element in dna_str)
shortest=min(len(element) for element in dna_str)

output=[]
flag_1,flag_2 = 1,1

for i in range(longest,shortest-1,-1):
    procent=sum(len(element) for element in dna_str if len(element) >= i)/total_legth
    if flag_1:
        if procent > 0.5:
            output.append(i)
            flag_1 = 0
    if flag_2:
        if procent > 0.75:
            output.append(i)
            flag_2 = 0
            break

print(*output)