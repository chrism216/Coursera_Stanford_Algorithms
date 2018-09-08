from random import choice
from math import log
from copy import deepcopy


def merge_vertex(adj):
    vertex1 = choice(list(adj))
    vertex2 = choice(adj[vertex1])
    vertex2_items = adj.pop(vertex2)

    # Add edges from deleted vertex2 to vertex1
    adj[vertex1] += vertex2_items

    #print("Merging vertices %s and %s:" %(vertex1, vertex2))
    
    # Update edges that pointed to vertex2
    for vertex, edges in adj.items():
        for i, edge in enumerate(edges):
            if edge == vertex2:
                adj[vertex][i] = vertex1

    # Delete self loops (connections in vertex1 that point to self):
    adj[vertex1] = list(filter(lambda x: x != vertex1, adj[vertex1]))

def karger_merge(adj):
    """Performs merges until only 2 nodes left, return number of edges in final cut"""
    while len(adj) > 2:
        merge_vertex(adj)
        edges_in_cut = len(adj[list(adj.keys())[0]])
    return edges_in_cut

def min_cut_batch(adj):
    """runs a batch of size n**2*log(n), returns the smallest cut found"""
    n = len(adj)
    num_runs = int(n**2 * log(n)) # Watch out for large n.
    print("Size of batch is: %s" % num_runs)
    print("Running...")

    min_cut = 1000
    for i in range(num_runs):
        copy = deepcopy(adj)
        # print(copy)
        this_cut = karger_merge(copy)
        if this_cut < min_cut:
            min_cut = this_cut
    return min_cut


if __name__ == "__main__":
    adj = {}
    adj[1] = [2, 3, 4, 7]
    adj[2] = [1, 7]
    adj[3] = [1, 4, 5]
    adj[4] = [1, 3, 6, 7]
    adj[5] = [3, 6, 7]
    adj[6] = [4, 5, 7]
    adj[7] = [1, 2, 4, 5, 6]

    print(min_cut_batch(adj))