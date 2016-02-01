import os
import sys
import networkx as nx


def main():
    
    G = nx.Graph()

    for line in open(sys.argv[1], 'r'):
        p1, p2 = line.rstrip().split()
        # nx will not add duplicate edges, neither (A,B) or (B,A)
        G.add_edge(p1, p2)

    G = sorted(nx.connected_component_subgraphs(G), key = len, reverse=True)[0]


    outfile = open(sys.argv[2], 'w')

    for n1 in G.nodes():
        outfile.write("{}\n".format(n1))

if __name__ == "__main__":
    main()
