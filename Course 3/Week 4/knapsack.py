import numpy as np
from sys import setrecursionlimit

class Knapsack():
    def __init__(self, total_capacity, values, weights):
        self.values = values
        self.weights = weights
        self.total_capacity = total_capacity
        self.n = len(values)
        self.memo = [[0] * (self.total_capacity + 1) for _ in range(self.n)]
        self.fill()

    def fill(self):
        for i in range(1, self.n):
            for x in range(0, self.total_capacity + 1):
                if self.weights[i] > x:
                    self.memo[i][x] = self.memo[i-1][x]
                else:
                    self.memo[i][x] = max(self.memo[i-1][x], self.memo[i-1][x - weights[i]] + values[i])
                
    @property
    def opimal_score(self):
        return self.memo[-1][-1]
    

class Knapsack_big():
    def __init__(self, total_capacity, values, weights):
        self.values = values
        self.weights = weights
        self.total_capacity = total_capacity
        self.memo = {}
        setrecursionlimit(4000)
        self.recursive_knapsack(len(self.values) - 1, total_capacity)
    
    def recursive_knapsack(self, i, x):
        if i == 0:
            return 0
        if (i, x) in self.memo:
            return self.memo[(i, x)]
        else:
            if x - weights[i] < 0:
                self.memo[(i, x)] = self.recursive_knapsack(i - 1, x)
            else:
                if self.recursive_knapsack(i - 1, x) \
                        >= self.recursive_knapsack(i - 1, x - weights[i]) + values[i]:
                    self.memo[(i, x)] = self.recursive_knapsack(i - 1, x)
                else:
                    self.memo[(i, x)] = self.recursive_knapsack(i - 1, x - weights[i]) + values[i]
        return self.memo[(i, x)]
        

    @property
    def opimal_score(self):
        return self.memo[(len(self.values) - 1, self.total_capacity)]

        
if __name__ == "__main__":
    values, weights = [0], [0]
    with open("knapsack_big.txt") as f:
        for i, line in enumerate(f):
            if i == 0:
                knapsack_size = int(line.strip().split(" ")[0])
            else:
                value = int(line.strip().split(" ")[0])
                weight = int(line.strip().split(" ")[1])
                values.append(value)
                weights.append(weight)
    
    K = Knapsack_big(knapsack_size, values, weights)
    print(K.opimal_score)