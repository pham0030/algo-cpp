# python3

import sys
import queue


class Graph:

    def __init__(self, adj, cost):
        self.adj = adj
        self.cost = cost
        self.num_vertices = len(adj)

    def shortest_paths(self, s):
        # Initialization
        self.dist = [float('inf') for _ in range(self.num_vertices)]
        self.reachable = [0 for _ in range(self.num_vertices)]
        self.shortest = [1 for _ in range(self.num_vertices)]
        self.visited = [False for _ in range(self.num_vertices)]

        self.dist[s] = 0
        self.reachable[s] = 1

        # Run Bellman-Ford iterations ~ number of vertices - 1 times
        for i in range(self.num_vertices-1):
            for u in range(self.num_vertices):
                for v_idx, v in enumerate(self.adj[u]):
                    if self.dist[v] > self.dist[u] + self.cost[u][v_idx]:
                        self.dist[v] = self.dist[u] + \
                                       self.cost[u][v_idx]
                        self.reachable[v] = 1

        stack = []
        for u in range(self.num_vertices):
            for v_idx, v in enumerate(self.adj[u]):
                if self.dist[v] > self.dist[u] + self.cost[u][v_idx]:
                    if v not in stack:
                        stack.append(v)

        # Bread First Search all the vertices in stack
        # and its connected neighbourhood
        while stack:
            vertex = stack.pop(0)
            self.visited[vertex] = True
            self.shortest[vertex] = 0
            # add its neighbour to stack if it is not
            # visied yet or not in the stack
            for adj_vertex in self.adj[vertex]:
                if not self.visited[adj_vertex] and adj_vertex not in stack:
                    stack.append(adj_vertex)


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3],
                 data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    s = data[0]
    s -= 1
    graph = Graph(adj, cost)
    graph.shortest_paths(s)
    for x in range(n):
        if graph.reachable[x] == 0:
            print('*')
        elif graph.shortest[x] == 0:
            print('-')
        else:
            print(graph.dist[x])
