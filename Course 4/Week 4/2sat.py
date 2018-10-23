import sys
from collections import Counter, defaultdict

class two_sat_scc:
    def __init__(self, graph, graph_rev):
        self.__graph = graph
        self.satisfiable = True

        # Compute SCCs using kosaraju's algorithm
        dfs_loop_rev = DFS_loop(graph_rev)
        dfs_loop = DFS_loop(graph, order_dict=dfs_loop_rev.finishing_times)

        # Search for contradictions within SCCs using DFS. 
        # Search from leader nodes in reverse topological order
        self.propositions = set()
        for finishing_time in range(1, len(dfs_loop.finishing_times) + 1):
            node = dfs_loop.finishing_times[finishing_time]
            if node in dfs_loop.scc:
                for item in dfs_loop.scc[node]:
                    # Search SCC for contradictions
                    if -item in dfs_loop.scc[node]:
                        self.satisfiable = False
                        return
                    
                    # SCC contains an item that's already been decided. Skip SCC
                    if -item in self.propositions:
                        break
                    
                    self.propositions.add(item)

class DFS_loop:
    def __init__(self, graph, order_dict=None):
        self.scc = defaultdict(list)
        self.finishing_times = {}
        self.__leaders = {}
        self.__visited = set()
        self.__t = 0
        self.__s = None
        self.__graph = graph

        if order_dict is None:
            for i in sorted(self.__graph.keys(), reverse=True):
                if i not in self.__visited:
                    self.__s = i
                    self.__DFS(i)

        else:
            for k in range(max(order_dict.keys()), 0, -1):
                i = order_dict[k]
                if i not in self.__visited:
                    self.__s = i
                    self.__DFS(i)

    def __DFS(self, i):
        self.__visited.add(i)
        self.__leaders[i] = self.__s
        self.scc[self.__s].append(i)
        for j in self.__graph[i]: # Examine all edges (i, j) of node i
            if j not in self.__visited:
                self.__DFS(j)
        self.__t += 1
        self.finishing_times[self.__t] = i

        
if __name__ == "__main__":
    graph, graph_rev = defaultdict(set), defaultdict(set)
    with open("2sat6.txt") as f:
        for i, line in enumerate(f):
            if i == 0:
                n = int(line.strip())
            else:
                num1, num2 = map(int, line.strip().split(" "))
                graph[-num1].add(num2)
                graph[-num2].add(num1)
                graph_rev[num1].add(-num2)
                graph_rev[num2].add(-num1)

    sys.setrecursionlimit(2**20)
    scc = two_sat_scc(graph, graph_rev)
    print(scc.satisfiable)