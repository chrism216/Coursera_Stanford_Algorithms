from collections import defaultdict
from math import inf
import numpy as np


class Floyd_warshall():
    def __init__(self, graph, vertices_count):
        self.distances = np.full((vertices_count + 1, vertices_count + 1), np.inf)
        for i in range(vertices_count + 1):
            self.distances[i, i] = 0

        for tail in graph.keys():
            for head in graph[tail].keys():
                self.distances[tail, head] = graph[tail][head]

        for k in range(0, vertices_count + 1):
            print(k)
            for i in range(0, vertices_count + 1):
                for j in range(0, vertices_count + 1):
                    if self.distances[i, j] > self.distances[i, k] + self.distances[k, j]:
                        self.distances[i, j] = self.distances[i, k] + self.distances[k, j]
        
        for i in range(vertices_count + 1):
            if self.distances[i, i] < 0:
                self.distances = None
                break


if __name__ == "__main__":
    # Use in all-pairs shortest path
    # g1 and g2 both have negative cycles.
    graph = defaultdict(dict)
    with open("g3.txt") as f:
        for i, line in enumerate(f):
            if i == 0:
                vertices_count, edges_count = map(int, line.strip().split(" "))
            else:
                tail, head, weight = map(int, line.strip().split(" "))
                graph[tail][head] = weight

    F = Floyd_warshall(graph, vertices_count) # This is quite slow.
    print(F.distances)