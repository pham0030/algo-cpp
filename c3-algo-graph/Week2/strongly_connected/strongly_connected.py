# python3

import sys

sys.setrecursionlimit(200000)


class Graph:

    def reverse_graph(self, adj):
        reversed_adj = [[] for _ in range(len(adj))]
        for vertex in range(len(adj)):
            for adj_vertex in adj[vertex]:
                reversed_adj[adj_vertex].append(vertex)
        return reversed_adj

    def __init__(self, adj):
        self.adj = adj
        self.num_vertices = len(self.adj)
        self.visited = [False for _ in range(self.num_vertices)]
        self.order = []
        self.number_of_scc = 0
        self.reversed_adj = self.reverse_graph(self.adj)

    def toposort(self):
        def explore_sort(vertex):
            self.visited[vertex] = True
            for adj_vertex in self.adj[vertex]:
                if not self.visited[adj_vertex]:
                    explore_sort(adj_vertex)
            self.order.append(vertex)
        # First DFS to topologically sort vertices
        for vertex in range(self.num_vertices):
            if not self.visited[vertex]:
                explore_sort(vertex)

    def explore_reversed(self, vertex):
        self.visited[vertex] = True
        for adj_vertex in self.reversed_adj[vertex]:
            if not self.visited[adj_vertex]:
                self.explore_reversed(adj_vertex)

    def number_of_strongly_connected_components(self):
        # topologically sort the vertices
        self.toposort()
        # Reset for another DFS
        self.visited = [False for _ in range(len(adj))]

        # Explore the reversed graph
        while self.order:
            vertex = self.order.pop()
            if not self.visited[vertex]:
                self.explore_reversed(vertex)
                self.number_of_scc += 1

        return self.number_of_scc

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
    print(graph.number_of_strongly_connected_components())
