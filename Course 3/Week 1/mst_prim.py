import os
import heapq
from collections import defaultdict

def create_graph(file_name):
    this_folder = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(this_folder, file_name)

    graph = defaultdict(dict)
    with open(my_file) as f:
        for i, line in enumerate(f):
            if i > 0:
                data = list(map(int, line.strip().split(" ")))
                graph[data[0]][data[1]] = data[2]
                # Need both directions, since graph is undirected...
                graph[data[1]][data[0]] = data[2]
    return graph

def mst(graph):
    # Initialize variables
    heap = []
    explored = set()
    seed_vertex = list(graph.keys())[0]
    explored.add(seed_vertex)
    total_cost = 0
    for v2 in graph[seed_vertex]:
        cost = graph[seed_vertex][v2]
        heapq.heappush(heap, (cost, v2))

    # Pop element
    while bool(graph.keys() - explored):
        while True:
            min_cost, min_head = heapq.heappop(heap)
            if min_head not in explored:
                break

        # Update variables with popped element
        explored.add(min_head)
        total_cost += min_cost

        # Push new element
        for new_head in graph[min_head]:
            if new_head not in explored:
                heapq.heappush(heap, (graph[min_head][new_head], new_head))

    return total_cost

if __name__ == "__main__":
    graph = create_graph("edges.txt")
    print(mst(graph))