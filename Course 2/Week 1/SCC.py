import sys
from collections import Counter, defaultdict

class SCC:
    def __init__(self, graph, graph_rev):
        dfs_loop_rev = DFS_loop(graph_rev)
        dfs_loop = DFS_loop(graph, order_dict=dfs_loop_rev.finishing_times)
        self.scc = dict(Counter(dfs_loop.leaders.values()))

    @property
    def formatted_top5(self):
        values = sorted(self.scc.values(), reverse=True)[:5]
        while len(values) < 5:
            values.append(0)
        return repr(values).replace(" ", "")[1:-1]

class DFS_loop:
    def __init__(self, graph, order_dict=None):
        self.finishing_times = {}
        self.leaders = {}
        self.__visited = set()
        self.__t = 0
        self.__s = None
        self.__graph = graph

        for i in range(max(self.__graph.keys()), 0, -1):
            if order_dict is not None:
                # Traverse graph with order given in a lookup dict
                i = order_dict[i]

            if i not in self.__visited:
                self.__s = i
                self.__DFS(i)

    def __DFS(self, i):
        self.__visited.add(i)
        self.leaders[i] = self.__s
        for j in self.__graph[i]: # Examine all edges (i, j) of node i
            if j not in self.__visited:
                self.__DFS(j)
        self.__t += 1
        self.finishing_times[self.__t] = i

        
if __name__ == "__main__":
    graph, graph_rev = defaultdict(set), defaultdict(set)
    with open("SCC.txt") as f:
        for line in f:
            num1, num2 = map(int, line.strip().split(" "))
            graph[num1].add(num2)
            graph_rev[num2].add(num1)

    sys.setrecursionlimit(2**20)
    scc = SCC(graph, graph_rev) 
    print(scc.formatted_top5)