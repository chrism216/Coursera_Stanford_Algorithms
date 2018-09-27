class Node():
    def __init__(self, label):
        self.label = label
        self.parent = self
        self.size = 1
        self.rank = 0
    
    def __eq__(self, other):
        return self.label == other.label

    def __repr__(self):
        return str(self.label)

class DisjointSet():
    """also called union-find data structure"""
    def __init__(self):
        self.nodes = {}
        self.connected_components = 0
        self.leaders = {}

    def makeSet(self, node):
        if node.label in self.nodes:
            return
        self.nodes[node.label] = node
        self.leaders[node.label] = node
        self.connected_components += 1

    def find(self, node):
        # Includes path compression
        if node.label not in self.nodes:
            self.makeSet(node)
        if node.parent == node:
            return node.parent
        node.parent = self.find(node.parent)
        return node.parent

    def union(self, node1, node2):
        """ Unite self and node"""
        parent1 = self.find(node1)
        parent2 = self.find(node2)

        if parent1 == parent2:
            return

        if parent2.size > parent1.size:
            parent1, parent2 = parent2, parent1
        
        parent2.parent = parent1
        parent1.size += parent2.size
        self.leaders.pop(parent2.label)
        self.connected_components -= 1
