import os
import DisjointSet

def create_graph(file_name):
    this_folder = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(this_folder, file_name)
    graph_list = []
    with open(my_file) as f:
        for i, line in enumerate(f):
            if i > 0:
                v1, v2, cost = tuple(map(int, line.strip().split(" ")))
                graph_list.append((cost, v1, v2))
    graph_list.sort()
    return graph_list

def max_spacing_k_clustering(graph, k):
    disjoint_set = DisjointSet.DisjointSet()

    # Create sets
    for edge in graph:
        disjoint_set.makeSet(DisjointSet.Node(edge[1]))
        disjoint_set.makeSet(DisjointSet.Node(edge[2]))

    # Union until there's k sets
    for edge in graph:
        distance = edge[0]
        n1 = disjoint_set.nodes[edge[1]]
        n2 = disjoint_set.nodes[edge[2]]
        disjoint_set.union(n1, n2)
        if disjoint_set.connected_components == k - 1:
            break
    return distance

if __name__ == "__main__":
    graph = create_graph("clustering1.txt")
    print(max_spacing_k_clustering(graph, 4))