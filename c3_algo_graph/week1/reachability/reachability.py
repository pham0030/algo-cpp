# python3

import sys


class Graph:

    def __init__(self, adj):
        self.adj = adj
        self.num_vertices = len(adj)
        self.group = [None for _ in range(self.num_vertices)]
        self.visited = [False for _ in range(self.num_vertices)]
        self.num_connected_comp = 0

    def explore(self, v):
        self.visited[v] = True
        self.group[v] = self.num_connected_comp
        for adj_v in self.adj[v]:
            if not self.visited[adj_v]:
                self.explore(adj_v)

    def _build_graph(self):
        for vertex in range(self.num_vertices):
            if not self.visited[vertex]:
                self.explore(vertex)
                self.num_connected_comp += 1

    def is_reachable(self, x, y):
        return 1 if self.group[x] == self.group[y] else 0

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    x, y = data[2 * m:]
    adj = [[] for _ in range(n)]
    x, y = x - 1, y - 1
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    graph = Graph(adj)
    graph._build_graph()
    print(graph.is_reachable(x, y))
