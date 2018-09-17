import os, heapq
from collections import defaultdict
from math import inf
import heapq


def create_graph(file_name):
    print("Creating graph...", end=" ")
    
    this_folder = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(this_folder, file_name)
    
    graph = defaultdict(dict)
    with open(my_file) as f:
        for line in f:
            tail, *heads = line.strip().split("\t")
            graph[int(tail)] = {int(head.split(",")[0]):int(head.split(",")[1]) for head in heads}
    print("Done.")
    return graph


def dijkstra_naive(graph, source_vertex=1):
    """ Implements dijkstra without min heap, running time is O(n^2)"""
    shortest_path_dist = defaultdict(int)
    shortest_paths = defaultdict(list)
    explored = set()

    shortest_path_dist[source_vertex] = 0
    shortest_paths[source_vertex] = [source_vertex]
    explored.add(source_vertex)

    while bool(graph.keys() - explored):
        min_tail, min_head, min_dist = None, None, inf
        for tail in shortest_path_dist:
            for head in graph[tail]:
                if head not in explored:
                    dist = shortest_path_dist[tail] + graph[tail][head]
                    if dist < min_dist:
                        min_dist, min_tail, min_head = dist, tail, head

        shortest_path_dist[min_head] = min_dist
        shortest_paths[min_head] = shortest_paths[min_tail] + [min_head]
        explored.add(min_head)
    return shortest_path_dist


def dijkstra(graph, source_vertex=1):
    """ Implements dijkstra with min heap, running time is O(nlog(n)"""
    shortest_path_dist = defaultdict(int)
    shortest_paths = defaultdict(list)
    explored = set()

    shortest_path_dist[source_vertex] = 0
    shortest_paths[source_vertex] = [source_vertex]
    explored.add(source_vertex)

    # Init heap
    dist_heap = []
    for node in graph[source_vertex]:
        dist = graph[source_vertex][node]
        heapq.heappush(dist_heap, (dist, source_vertex, node))

    while bool(graph.keys() - explored):
        # Extract smallest unexplored item from heap
        while True:
            min_dist, min_tail, min_head = heapq.heappop(dist_heap)
            if min_head not in explored:
                break
        
        shortest_path_dist[min_head] = min_dist
        shortest_paths[min_head] = shortest_paths[min_tail] + [min_head]
        explored.add(min_head)

        # Push new items into heap
        for node in graph[min_head]:
            if node not in explored:
                dist = min_dist + graph[min_head][node]
                heapq.heappush(dist_heap, (dist, min_head, node))

    return shortest_path_dist

if __name__ == "__main__":
    graph = create_graph("dijkstraData.txt")
    shortest_paths = dijkstra(graph)

    for i in [7,37,59,82,99,115,133,165,188,197]:
        print(shortest_paths[i], end=",")
    print()