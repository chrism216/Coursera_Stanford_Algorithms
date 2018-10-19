from math import sqrt, inf

class TSP_heuristic:
    def __init__(self, vertices, starting_vertex=1):
        def sq_eucl_dist(point1, point2):
            return (point1[0] - point2[0])**2 + (point1[1] - point2[1])**2

        starting_vertex_coords = vertices[starting_vertex]
        distance = 0
        
        last_vertex_coords = vertices[starting_vertex]
        del vertices[starting_vertex]

        while vertices:
            min_distance = inf
            for i in vertices.keys():
                sq_dist = sq_eucl_dist(last_vertex_coords, vertices[i])
                if sq_dist < min_distance:
                    min_distance = sq_dist
                    min_i = i
            distance += sqrt(min_distance)
            last_vertex_coords = vertices[min_i]
            del vertices[min_i]

        distance += sqrt(sq_eucl_dist(last_vertex_coords, starting_vertex_coords))
        self.shortest_path = distance

if __name__ == "__main__":
    vertices = {}
    with open("nn.txt") as f:
        for i, line in enumerate(f):
            if i == 0:
                vertices_count =  int(line.strip())
            else:
                index, x, y = map(float, line.strip().split(" "))
                vertices[index] = (x, y)

    print(TSP_heuristic(vertices).shortest_path)