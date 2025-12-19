import math
from collections import deque
from heapq import heappush, heappop

coordinates = []
circuits = {}

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return
        if self.rank[ra] < self.rank[rb]:
            self.parent[ra] = rb
        elif self.rank[ra] > self.rank[rb]:
            self.parent[rb] = ra
        else:
            self.parent[rb] = ra
            self.rank[ra] += 1

with open('input8.txt') as file:
    for line in file:
        x, y, z = map(int, line.split(','))
        coordinates.append((x, y, z))

# NOW initialize circuits once, correctly:
circuits = {i: set() for i in range(len(coordinates))}

dsu = DSU(len(coordinates))

def is_connected(coordinate1_index, coordinate2_index):
    """
    Are two coordinates connected on the same circuit?
    :param coordinate1_index:
    :param coordinate2_index:
    :return:
    """
    if (coordinate1_index in circuits[coordinate2_index]
            and coordinate2_index in circuits[coordinate1_index]):
        return True
    return False


def connect(a, b):
    circuits[a].add(b)
    circuits[b].add(a)
    dsu.union(a, b)

def straight_line_dist(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2 + (coord1[2] - coord2[2]) ** 2)


def get_closest_unconnected(coordinates):
    closest1 = None
    closest2 = None
    closest_distance = math.inf
    for i, coordinate1 in enumerate(coordinates):
        for j, coordinate2 in enumerate(coordinates):
            if coordinate1 != coordinate2:
                dist = straight_line_dist(coordinate1, coordinate2)
                if dist < closest_distance and not is_connected(i, j):
                    closest1 = i
                    closest2 = j
                    closest_distance = dist
    return closest1, closest2, closest_distance


def connect_n_closest(n=10):
    edges_added = 0
    while edges_added < n:
        dist, i, j = heappop(distance_heap)
        if j not in circuits[i]:     # O(1) because circuits uses sets
            connect(i, j)
            edges_added += 1



def vertex_contained_in_component(components, vertex):
    for component in components:
        if vertex in component:
            return True
    return False

def find_connected_components(circuits):
    components = []
    for vertex in circuits:
        if not vertex_contained_in_component(components, vertex):
            queue = deque([vertex])
            visited = set()
            # breadth-first search to find all connected components of a vertex
            while queue:
                curr_vertex = queue.popleft()
                visited.add(curr_vertex)

                for neighbor in circuits[curr_vertex]:
                    if neighbor not in visited:
                        queue.append(neighbor)

            components.append(visited)
    return components

def build_distance_heap():
    heap = []
    N = len(coordinates)
    for i in range(N):
        for j in range(i+1, N):
            d = straight_line_dist(coordinates[i], coordinates[j])
            heappush(heap, (d, i, j))
    return heap


def connect_until_all_connected():
    i = j = -1

    while True:
        root = dsu.find(0)
        all_connected = all(dsu.find(x) == root for x in range(len(coordinates)))
        if all_connected:
            return i, j

        dist, i, j = heappop(distance_heap)
        if j not in circuits[i]:
            connect(i, j)

distance_heap = build_distance_heap()
connect_n_closest(1000)
components = find_connected_components(circuits)
sorted_components = sorted(components, key=len, reverse=True)

print(f"Product of 3 largest circuits is {len(sorted_components[0])*len(sorted_components[1])*len(sorted_components[2])}")

coord1, coord2 = connect_until_all_connected()
print(f"Coordinates of last 2 to connect are {coordinates[coord1]} and {coordinates[coord2]}")