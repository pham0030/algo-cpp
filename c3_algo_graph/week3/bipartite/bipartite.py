# python3

import sys
import queue


class Graph:

    def __init__(self, adj):
        self.adj = adj
        self.num_vertices = len(self.adj)
        self.partition = [0 for _ in range(self.num_vertices)]
        self.visited = [False for _ in range(self.num_vertices)]

    def bipartite(self):
        q = queue.Queue()

        # initialize first vertex
        self.partition[0] = 0
        q.put(0)

        while not q.empty():
            vertex = q.get()
            for adj_vertex in self.adj[vertex]:
                if self.visited[adj_vertex] is True and \
                   self.partition[vertex] == self.partition[adj_vertex]:
                    return 0
                else:
                    if not self.visited[adj_vertex]:
                        self.visited[adj_vertex] = True
                        self.partition[adj_vertex] = 1 - self.partition[vertex]
                        q.put(adj_vertex)
        return 1

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
    graph = Graph(adj)
    print(graph.bipartite())
