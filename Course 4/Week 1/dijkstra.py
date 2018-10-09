import os, heapq
from math import inf
from collections import defaultdict
import heapq

class Dijkstra():
    def __init__(self, graph, vertices_count, source_vertex=1):
        self.shortest_path_dist = {}
        self.shortest_paths = {}
        self.explored = set()

        self.shortest_path_dist[source_vertex] = 0
        self.shortest_paths[source_vertex] = [source_vertex]
        self.explored.add(source_vertex)

        # Init heap
        dist_heap = []
        for node in graph[source_vertex]:
            dist = graph[source_vertex][node]
            heapq.heappush(dist_heap, (dist, source_vertex, node))

        while bool(graph.keys() - self.explored):
            # Extract smallest unexplored item from heap
            while True:
                min_dist, min_tail, min_head = heapq.heappop(dist_heap)
                if min_head not in self.explored:
                    break

            self.shortest_path_dist[min_head] = min_dist
            self.shortest_paths[min_head] = self.shortest_paths[min_tail] + [min_head]
            self.explored.add(min_head)

                    # Push new items into heap
            for node in graph[min_head]:
                if node not in self.explored:
                    dist = min_dist + graph[min_head][node]
                    heapq.heappush(dist_heap, (dist, min_head, node))


if __name__ == "__main__":
    # Use in all-pairs shortest path
    # g1 and g2 both have negative cycles.
    graph = defaultdict(dict)
    with open("test.txt") as f:
        for i, line in enumerate(f):
            if i == 0:
                vertices_count, edges_count = map(int, line.strip().split(" "))
            else:
                tail, head, weight = map(int, line.strip().split(" "))
                graph[tail][head] = weight

    D = Dijkstra(graph, vertices_count)
    print(D.shortest_path_dist)
