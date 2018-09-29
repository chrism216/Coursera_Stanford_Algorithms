import heapq

class Node():
    def __init__(self, weight, label=None, left_child=None, right_child=None):
        self.weight = weight
        self.label = label
        self.left_child = left_child
        self.right_child = right_child

    def merge(self, other):
        parent_weight = self.weight + other.weight
        parent_node = Node(parent_weight,left_child=self, right_child=other)
        return parent_node

    def __eq__(self, other):
        return self.weight == other.weight

    def __lt__(self, other):
        return self.weight < other.weight

    def __le__(self, other):
        return self.weight <= other.weight

    def __gt__(self, other):
        return self.weight > other.weight

    def __ge__(self, other):
        return self.weight >= other.weight


class Encoding():
    def __init__(self, root_node):
        self.encoding = {}
        self.get_encoding(root_node, "")

    def get_encoding(self, node, code):
        if node.label:
            self.encoding[node.label] = code
            return
        self.get_encoding(node.left_child, "0" + code)
        self.get_encoding(node.right_child, "1" + code)


def huffman_coding(weights):
    heap = [Node(weights[i], label=i) for i in weights.keys()]
    heapq.heapify(heap)
    while len(heap) > 1:
        n1 = heapq.heappop(heap)
        n2 = heapq.heappop(heap)
        new_root = n1.merge(n2)
        heapq.heappush(heap, new_root)
    E = Encoding(new_root)
    return E.encoding


if __name__ == "__main__":
    weights = {}
    with open("huffman.txt") as f:
        for i, line in enumerate(f):
            if i > 0:
                weight = int(line.strip())
                weights[i] = weight

    encoding = huffman_coding(weights)
    lengths = [len(encoding[i]) for i in encoding.keys()]
    print(max(lengths))
    print(min(lengths))