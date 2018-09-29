class Mwis():
    def __init__(self, graph):
        self.memo = []
        self.solution = []
        self.graph = graph
        self.memo.append(0)
        self.memo.append(graph[1])
        self.calculate_mwis()
        self.reconstruct()

    def calculate_mwis(self):
        for i in range(2, len(graph)):
            self.memo.append(max(self.memo[i-1], self.memo[i-2] + self.graph[i]))

    def reconstruct(self):
        self.solution = set()
        i = len(self.memo) - 1
        while i >= 1:
            if self.memo[i-1] >= self.memo[i-2] + self.graph[i]:
                i -= 1
            else:
                self.solution.add(i)
                i -= 2

if __name__ == "__main__":
    graph = [0] # We're counting from index 1. Ignore zeroth index
    with open("mwis.txt") as f:
        for i, line in enumerate(f):
            if i > 0:
                graph.append(int(line.strip()))
    
    sol = Mwis(graph).solution
    for i in (1, 2, 3, 4, 17, 117, 517, 997):
        if i in sol:
            print("1", end="")
        else:
            print("0", end="")
    print()