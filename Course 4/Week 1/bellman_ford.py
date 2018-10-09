from collections import defaultdict
from math import inf


class Bellman_ford():
    def __init__(self, graph, vertices_count, source_vertex=1):
        self.graph = graph
        self.vertices_count = vertices_count
        self.early_abort = False

        self.distances = defaultdict(lambda: inf)
        self.distances[source_vertex] = 0
        self.node_predecessors = {}

        self._compute_shortest_paths()
        if not self.early_abort:
            self._test_negative_cycles()

    def _single_iteration(self):
        modified = False
        for tail in list(self.graph.keys()):
            for head in self.graph[tail]:
                if self.distances[tail] + self.graph[tail][head] < self.distances[head]:
                    self.distances[head] = self.graph[tail][head] + self.distances[tail]
                    self.node_predecessors[head] = tail
                    modified = True
        return modified

    def _compute_shortest_paths(self):
        for _ in range(self.vertices_count):
            if not self._single_iteration():
                self.early_abort = True
                return
    
    def _test_negative_cycles(self):
        if self._single_iteration():
            self.distances = None
            self.node_predecessors = None
            print("Negative cycle detected!")

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
    
    min_dist = inf
    for i in range(1, vertices_count + 1):
        B = Bellman_ford(graph, vertices_count, source_vertex=i)
        min_this_iter = min(B.distances.values())
        if min_this_iter < min_dist:
            min_dist = min_this_iter
        print(i, min_dist)

    print(min_dist)


                