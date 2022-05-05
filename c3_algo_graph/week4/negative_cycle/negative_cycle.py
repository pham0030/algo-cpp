# python3

import sys


class Graph:

    def __init__(self, adj, cost):
        self.adj = adj
        self.cost = cost
        self.num_vertices = len(self.adj)
        # dist should be initialized = 0 not inf as in the lecture notes
        self.dist = [0 for _ in range(self.num_vertices)]
        self.prev = [None for _ in range(self.num_vertices)]

    def negative_cycle(self):
        self.dist[0] = 0
        # Run Bellman-Ford iterations ~ number of vertices times
        for i in range(self.num_vertices):
            for u in range(self.num_vertices):
                for v_idx, v in enumerate(self.adj[u]):
                    if self.dist[v] > self.dist[u] + self.cost[u][v_idx]:
                        self.dist[v] = self.dist[u] + \
                                       self.cost[u][v_idx]
                        self.prev[v] = u
        for u in range(self.num_vertices):
            for v_idx, v in enumerate(self.adj[u]):
                if self.dist[v] > self.dist[u] + self.cost[u][v_idx]:
                    return 1
        return 0


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
    graph = Graph(adj, cost)
    print(graph.negative_cycle())
