# python3
import sys
import math


class Node:

    def __init__(self, idx, x, y, root):
        self.idx = idx
        self.x = x
        self.y = y
        self.root = root
        self.rank = 0


class Edge:

    def __init__(self, u, v):  # Node u and Node v
        self.u = u
        self.v = v
        self.dist = self.distance(u, v)

    def distance(self, u, v):
        return math.sqrt(math.pow(u.x-v.x, 2) + math.pow(u.y-v.y, 2))


class Graph:

    def __init__(self, x, y, k):
        self.n = len(x)
        self.k = k
        self.n_clusters = self.n
        self.nodes = []
        self.edges = []
        for i in range(self.n):
            node_i = Node(i, x[i], y[i], i)
            self.nodes.append(node_i)
            for j in range(i+1, self.n):
                node_j = Node(j, x[j], y[j], j)
                self.edges.append(Edge(node_i, node_j))

    # Disjoint set implementation
    def Find(self, node):  # find the set of node i
        i = node.idx
        if i != self.nodes[i].root:
            self.nodes[i].root = self.Find(self.nodes[node.root])
        return self.nodes[i].root

    def Union(self, u, v):
        set_u = self.Find(u)
        set_v = self.Find(v)

        if set_u != set_v:
            if self.nodes[set_u].rank > self.nodes[set_v].rank:
                self.nodes[set_v].root = set_u
            else:
                self.nodes[set_u].root = set_v
                if self.nodes[set_u].rank == self.nodes[set_v].rank:
                    self.nodes[set_v].rank += 1
            self.n_clusters -= 1

    def clustering(self):
        # Sorting the edges in non-decreasing dist order
        self.edges = sorted(self.edges, key=lambda edge: edge.dist)

        for edge in self.edges:
            if self.Find(edge.u) != self.Find(edge.v):
                self.Union(edge.u, edge.v)
            if self.n_clusters == self.k - 1:
                return edge.dist


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    data = data[1:]
    x = data[0:2 * n:2]
    y = data[1:2 * n:2]
    data = data[2 * n:]
    k = data[0]
    graph = Graph(x, y, k)
    print("{0:.9f}".format(graph.clustering()))
