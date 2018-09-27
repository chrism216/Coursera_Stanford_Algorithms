import os
import DisjointSet

def create_graph(file_name):
    this_folder = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(this_folder, file_name)
    graph_set = set()
    with open(my_file) as f:
        for i, line in enumerate(f):
            if i > 0:
                graph_set.add(int(line.strip().replace(" ", ""), 2))
    return graph_set

def hamming_distance_1_candidates(x):
    bits = 24
    candidates = set()
    for i in range(bits):
        candidates.add(x ^ (1 << i))
    return candidates

def hamming_distance_2_candidates(x):
    bits = 24
    candidates = set()
    for i in range(bits):
        for j in range(i + 1, bits):
            candidates.add(x ^ (1 << i) ^ (1 << j))
    return candidates


def max_spacing_k_clustering_big(graph_set):
    disjoint_set = DisjointSet.DisjointSet()

    # Create sets
    for node in list(graph_set):
        disjoint_set.makeSet(DisjointSet.Node(node))

    # Merge distance 1 nodes
    for node in list(graph_set):
        candidates = hamming_distance_1_candidates(node)
        matches = candidates & graph_set
        for match in list(matches):
            n1 = disjoint_set.nodes[match]
            n2 = disjoint_set.nodes[node]
            disjoint_set.union(n1, n2)

    # Merge distance 2 nodes
    for node in list(graph_set):
        candidates = hamming_distance_2_candidates(node)
        matches = candidates & graph_set
        for match in list(matches):
            n1 = disjoint_set.nodes[match]
            n2 = disjoint_set.nodes[node]
            disjoint_set.union(n1, n2)
    return disjoint_set.connected_components

if __name__ == "__main__":
    graph = create_graph("clustering_big.txt")
    print(max_spacing_k_clustering_big(graph))
