import sys, os
dn=os.path.dirname(__file__)
pdn=os.path.join(dn,"..")
sys.path.append(pdn)
import utils
#sys.path.append(os.path.join(pdn,"/dbru"))
import networkx as nx

inFile = sys.argv[1]

with open(inFile,"r") as file:
    lines = map(str.strip, file.readlines())
    kmers=set()
    for line in lines:
        kmers.add((line[:-1], line[1:]))
        rc=utils.revc(line)
        kmers.add((rc[:-1],rc[1:]))

    edge_list=[]    
    for (a,b) in sorted(kmers):
        edge_list.append((a,b,1))

G=nx.Graph()
G.add_weighted_edges_from(edge_list)
output=list(nx.find_cycle(G))

chromosone=''

for i in range(len(output)):
    chromosone+=(output[i][0][0])

print(utils.revc(chromosone))
