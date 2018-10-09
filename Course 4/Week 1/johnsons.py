from dijkstra import Dijkstra
from bellman_ford import Bellman_ford
from collections import defaultdict


class Johnsons():
    def __init__(self, graph, vertices_count):
        self.graph = graph

        extra_vertex = {}
        for tail in graph.keys():
            for head in graph[tail]:
                extra_vertex[tail] = 0
                extra_vertex[head] = 0
        
        self.graph[0] = extra_vertex
        B = Bellman_ford(self.graph, vertices_count + 1, source_vertex=0)
        self.p_values = B.distances
        self.graph.pop(0)
        
        self.graph_double_prime = defaultdict(dict)
        for tail in graph.keys():
            for head in graph[tail]:
                self.graph_double_prime[tail][head] = graph[tail][head] + self.p_values[tail] - self.p_values[head]
        
        self.shortest_paths_dist_prime = {}
        for i in range(1, vertices_count +1 ):
            print(i)
            D = Dijkstra(self.graph_double_prime, vertices_count, source_vertex=i)
            for j in D.shortest_path_dist.keys():
                self.shortest_paths_dist_prime[(i, j)] = D.shortest_path_dist[j]

        self.shortest_path_dist = {}
        for tail, head in self.shortest_paths_dist_prime.keys():
            self.shortest_path_dist[(tail, head)] = self.shortest_paths_dist_prime[(tail, head)] - self.p_values[tail] + self.p_values[head]


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

    J = Johnsons(graph, vertices_count)
    print(min(J.shortest_path_dist.values()))