# python3

import sys
import queue


class Graph:

    def __init__(self, adj):
        self.adj = adj
        self.num_vertices = len(self.adj)
        self.dist = [-1 for _ in range(self.num_vertices)]

    def distance(self, s, t):
        self.dist[s] = 0
        q = queue.Queue()
        q.put(s)
        while not q.empty():
            vertex = q.get()
            for adj_vertex in self.adj[vertex]:
                if self.dist[adj_vertex] == -1:
                    q.put(adj_vertex)
                    self.dist[adj_vertex] = self.dist[vertex] + 1

        return self.dist[t]


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    graph = Graph(adj)
    print(graph.distance(s, t))
