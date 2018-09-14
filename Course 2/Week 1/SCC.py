import os, sys
from collections import Counter, defaultdict


class Book_keeping():
    def __init__(self):
        self.visited = set()
        self.finishing_times = {}
        self.leaders = {}
        self.t = 0
        self.s = None

def DFS_loop(graph, book_keeping, order_dict=None):
    for i in range(max(graph.keys()), 0, -1):
        if order_dict is not None:
            # Traverse graph with order given in a lookup dict
            i = order_dict[i]

        if i not in book_keeping.visited:
            book_keeping.s = i
            DFS(graph, i, book_keeping)

def DFS(graph, i, book_keeping):
    book_keeping.visited.add(i)
    book_keeping.leaders[i] = book_keeping.s
    for j in graph[i]: # Examine all edges (i, j) of node i
        if j not in book_keeping.visited:
            DFS(graph, j, book_keeping)
    book_keeping.t += 1
    book_keeping.finishing_times[book_keeping.t] = i

def create_graphs(file_name):
    print("Creating graphs...", end=" ", flush=True)
    graph, graph_rev = defaultdict(set), defaultdict(set)
    this_folder = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(this_folder, file_name)
    with open(my_file) as f:
        for line in f:
            num1, num2 = map(int, line.strip().split(" "))
            graph[num1].add(num2)
            graph_rev[num2].add(num1)
    print("Done.")
    return graph, graph_rev

def SCCs(graph, graph_rev):
    book_keeping1 = Book_keeping()
    book_keeping2 = Book_keeping()

    print("Running DFS on reverse graph...", end=" ", flush=True)
    DFS_loop(graph_rev, book_keeping1)
    print("Done.")

    print("Running DFS on forward graph...", end=" ", flush=True)
    DFS_loop(graph, book_keeping2, order_dict=book_keeping1.finishing_times)
    print("Done.")

    scc = dict(Counter(book_keeping2.leaders.values()))
    return scc

def formatted_top5(scc):
    values = sorted(scc.values(), reverse=True)[:5]
    while len(values) < 5:
        values.append(0)
    return repr(values).replace(" ", "")[1:-1]
        

if __name__ == "__main__":
    sys.setrecursionlimit(2**20)
    scc = SCCs(*create_graphs("SCC.txt"))
    print("Top 5 SCC:", formatted_top5(scc))