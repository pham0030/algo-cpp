# python3

import sys
import queue
from functools import total_ordering


@total_ordering
class Vertex:

    def __init__(self, index, distance):
        self.index = index
        self.distance = distance

    def __lt__(self, other):
        return self.distance < other.distance

    def __eq__(self, other):
        return self.distance == other.distance


class Graph:

    def __init__(self, adj, cost):
        self.adj = adj
        self.cost = cost
        self.num_vertices = len(self.adj)
        self.dist = [float('inf') for _ in range(self.num_vertices)]
        self.prev = [None for _ in range(self.num_vertices)]

    def distance(self, s, t, verbose=False):
        self.dist[s] = 0
        priority_queue = queue.PriorityQueue()
        priority_queue.put(Vertex(s, self.dist[s]))

        while not priority_queue.empty():
            u = priority_queue.get()
            u_index = u.index
            for v in self.adj[u_index]:
                v_cost_index = self.adj[u_index].index(v)
                if self.dist[v] > self.dist[u_index] + \
                   self.cost[u_index][v_cost_index]:
                    self.dist[v] = self.dist[u_index] + \
                                   self.cost[u_index][v_cost_index]
                    self.prev[v] = u_index
                    priority_queue.put(Vertex(v, self.dist[v]))
        if self.dist[t] == float('inf'):
            return -1
        return self.dist[t]


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]),
                 data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    s, t = data[0] - 1, data[1] - 1
    graph = Graph(adj, cost)
    print(graph.distance(s, t))
