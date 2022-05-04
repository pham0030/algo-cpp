# python3
import sys


class Graph:

    def __init__(self, adj):
        self.adj = adj
        self.num_vertices = len(adj)
        self.visited = [False for _ in range(self.num_vertices)]
        self.order = []

    def _explore(self, vertex):
        self.visited[vertex] = True
        for adj_vertex in self.adj[vertex]:
            if not self.visited[adj_vertex]:
                self._explore(adj_vertex)
        self.order.append(vertex)

    def _toposort(self):
        for vertex in range(self.num_vertices):
            if not self.visited[vertex]:
                self._explore(vertex)
        self.order.reverse()

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    graph = Graph(adj)
    graph._toposort()
    order = graph.order
    for x in order:
        print(x + 1, end=' ')
