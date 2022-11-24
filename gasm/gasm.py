import sys, os
dn=os.path.dirname(__file__)
pdn=os.path.join(dn,"..")
sys.path.append(pdn)
import utils
import networkx as nx

inFile = sys.argv[1]
#beolvassuk a reszleteket
with open(inFile) as input_data:
    k_mers = [line.strip() for line in input_data.readlines()]

#ilyen hosszuak a reszletek
length=len(k_mers[0])

#keressuk azt a k-t, amire pont ketto kor lesz a de bruijn grafban
for j in range(1,length):
    #halmazba gyujtom az eleket
    dbg_nodes_elements=set()
    for kmer in k_mers:
        for i in range(j):
            #begyujtom az osszes k hosszu kmert, ezek nem csak az elejen lehetnek, hanem kesobb is kezdodhetnek
            #de ez a j valtozo lesz
            dbg_nodes_elements.add(kmer[i:len(kmer)+i-j+1])
            dbg_nodes_elements.add(utils.revc(kmer[i:len(kmer)-j+i+1]))
    k=len(list(dbg_nodes_elements)[0])
    G=nx.Graph()
    G.add_nodes_from(dbg_nodes_elements)
    #definialom, mik az elek
    edge = lambda element: [element[0:k-1],element[1:k]]
    dbg_edges = [edge(element) for element in dbg_nodes_elements]
    G.add_edges_from(dbg_edges)

    #nx talal koroket, ha ketto van, ahogy a feladata allitja, akkor jok vagyunk
    circles=nx.cycle_basis(G)
    cyclic_superstring=''
    if len(circles)==2:
        for edge in circles[0]:
            cyclic_superstring += edge[0]
        print(utils.revc(cyclic_superstring))
        break