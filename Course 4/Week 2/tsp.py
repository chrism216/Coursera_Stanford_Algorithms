from collections import defaultdict
from math import sqrt, inf
from itertools import permutations, combinations

class TSP():
    def __init__(self, points):
        self.n = len(points)
        self.distances = {}
        for i in permutations(range(self.n), 2):
            self.distances[i] = euclidian_dist(points[i[0]], points[i[1]])

        A = defaultdict(lambda: inf)
        for S in self.generate_sets(1):
            A[(S, 0)] = 0
        
        for m in range(2, self.n + 1):
            for S in self.generate_sets(m):
                for j in S:
                    if j !=0:
                        A[(S, j)] = min([A[(self.filtered_set(S, j), k)] + 
                            self.distances[(k, j)] for k in self.filtered_set(S, j)])
        self.shortest_path = min([A[(tuple(range(self.n)), j)] + self.distances[(j, 0)] for j in range(1, self.n)])
    
    def generate_sets(self, m):
        combs = combinations(range(1, self.n), m - 1)
        for comb in combs:
            yield (0, ) + comb

    def filtered_set(self, tup, elem):
        l = list(tup)
        l.remove(elem)
        return tuple(l)

def euclidian_dist(p1, p2):
    return sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)


if __name__ == "__main__":
    vertices = []
    with open("tsp.txt") as f:
        for i, line in enumerate(f):
            if i == 0:
                vertices_count =  int(line.strip())
            else:
                x, y = map(float, line.strip().split(" "))
                vertices.append((x, y))

    # Breaking up graph into 2 smaller graphs makes it faster (though not guaranteed to be
    # correct). See forum tips. Nodes 11 and 12 included in both graphs, then their 
    # corresponding edge is subtracted twice.           
    v1 = vertices[:13]
    v2 = vertices[11:]
    tsp1 = TSP(v1)
    tsp2 = TSP(v2)
    ans = tsp1.shortest_path + tsp2.shortest_path - 2 * tsp1.distances[(11, 12)]
    print(ans)