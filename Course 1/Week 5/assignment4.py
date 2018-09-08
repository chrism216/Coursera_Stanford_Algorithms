import os
import kargerMinCut

this_folder = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(this_folder, 'kargerMinCut.txt')

adj = {}
with open(my_file) as f:
    for line in f:
        data = list(map(int, line.strip().split("\t")))
        adj[data[0]] = data[1:]

print(kargerMinCut.min_cut_batch(adj))