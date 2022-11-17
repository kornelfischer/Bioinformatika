import sys
import networkx as nx

inFile = sys.argv[1]

def tree(my_file="test.txt"):
    u_nodes=[]
    v_nodes=[]
    with open(my_file,"r") as file:
        for idx,line in enumerate(file):
            if idx==0:
                number_of_nodes=int(line)
                continue
            line=line.split()
            u_nodes.append(int(line[0]))
            v_nodes.append(int(line[1]))
    G = nx.Graph()
    G.add_nodes_from([i+1 for i in range(number_of_nodes)])
    G.add_edges_from(zip(u_nodes,v_nodes))
    if not nx.is_forest(G):
        print("It is not a tree")
    print(number_of_nodes-1-len(G.edges))


tree(inFile)