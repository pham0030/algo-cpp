# python3
import sys


class Graph:

    def __init__(self, adj):
        self.adj = adj
        self.num_vertices = len(adj)
        self.status = ["NOTPROCESSED" for _ in range(self.num_vertices)]

    def graph_cyclic(self):

        def is_cyclic(vertex):  # follow one vertex
            self.status[vertex] = "PROCESSING"
            for adj_vertex in self.adj[vertex]:
                if self.status[adj_vertex] == "PROCESSING":
                    return True
                if self.status[adj_vertex] == "NOTPROCESSED" and \
                   is_cyclic(adj_vertex) is True:
                    return True
            self.status[vertex] = "PROCESSED"
            return False

        for vertex in range(self.num_vertices):  # check all the vertices
            if self.status[vertex] == "NOTPROCESSED":
                if is_cyclic(vertex):
                    return True
        return False

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
    print(1 if graph.graph_cyclic() else 0)
