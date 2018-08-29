from math import sqrt
import numpy as np

def euclidian_dist(p1, p2):
    return sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def closest_pair_brute(points):
    distance = -1
    for i in range(len(points)):
        for j in range(len(points)):
            if i != j:
                curr_dist = euclidian_dist(points[i], points[j])
                if curr_dist < distance or distance < 0:
                    distance = curr_dist
    return distance

def closest_pair(points):
    if len(points) <= 3:
        return closest_pair_brute(points)
    else:    
        n = len(points)
        half = n // 2
        L, R = points[:half], points[half:]
        distance = min(closest_pair(L), closest_pair(R))
        x_split = points[half][0]

        slit = points[(points[:,0] > x_split - distance) | (points[:,0] < x_split + distance)]
        Sy = slit[slit[:,1].argsort()]

        dist_sy = distance
        for k in range(len(Sy)):
            for c in range(k + 1, min(k + 7, len(Sy))):
                if euclidian_dist(Sy[k], Sy[c]) < dist_sy:
                    dist_sy = euclidian_dist(Sy[k], Sy[c])
    return min(dist_sy, distance)

if __name__ == "__main__":
    # Generate list of random points
    n = 1000

    points = np.random.uniform(low=0, high=10, size=(n, 2))
    points = points[points[:,0].argsort()]

    print(closest_pair(points))
    print(closest_pair_brute(points))
    # It's much faster then the brute force approach...