# python3


class Edge:

    def __init__(self, u, v, capacity):
        self.u = u
        self.v = v
        self.capacity = capacity
        self.flow = 0


# This class implements a bit unusual scheme for storing edges of the graph,
# in order to retrieve the backward edge for a given edge quickly.
class FlowGraph:

    def __init__(self):
        pass

    def add_edge(self, from_, to, capacity):
        # Note that we first append a forward edge and then a backward edge,
        # so all forward edges are stored at even indices (starting from 0),
        # whereas backward edges are stored at odd indices.
        forward_edge = Edge(from_, to, capacity)
        backward_edge = Edge(to, from_, 0)
        self.graph[from_].append(len(self.edges))
        self.edges.append(forward_edge)
        self.graph[to].append(len(self.edges))
        self.edges.append(backward_edge)

    def read_data(self):
        vertex_count, edge_count = map(int, input().split())
        # List of all - forward and backward - edges
        self.edges = []
        # These adjacency lists store only indices of edges in the edges list
        self.graph = [[] for _ in range(vertex_count)]
        for _ in range(edge_count):
            u, v, capacity = map(int, input().split())
            self.add_edge(u - 1, v - 1, capacity)

    def size(self):
        return len(self.graph)

    def get_ids(self, from_):
        return self.graph[from_]

    def get_edge(self, id):
        return self.edges[id]

    def add_flow(self, id, flow):
        # To get a backward edge for a true forward edge (i.e id is even),
        # we should get id + 1
        # due to the described above scheme. On the other hand, when we have
        # to get a "backward"
        # edge for a backward edge (i.e. get a forward edge for backward
        # - id is odd), id - 1 should be taken.
        #
        # It turns out that id ^ 1 works for both cases. Think this through!
        self.edges[id].flow += flow
        self.edges[id ^ 1].flow -= flow

    def bfs(self, from_, to):
        queue = []
        queue.append(from_)
        visited = [False] * self.size()
        prev = {}

        while queue:
            current = queue.pop(0)
            visited[current] = True
            edge_ids = self.get_ids(current)
            for edge_id in edge_ids:
                edge = self.get_edge(edge_id)
                if not visited[edge.v] and edge.capacity > edge.flow:
                    prev[edge.v] = current
                    queue.append(edge.v)
                    if edge.v == to:
                        return prev

    def recalculate_flow(self, to, prev):
        current = to
        min_cap = float('inf')
        path = []
        while True:
            previous = prev[current]
            edge_ids = self.get_ids(previous)
            for edge_id in edge_ids:
                edge = self.get_edge(edge_id)
                if edge.v == current and edge.u == previous and \
                   edge.capacity > edge.flow:
                    path.append(edge_id)
                    min_cap = min(min_cap, edge.capacity - edge.flow)
                    break
            current = previous
            if previous == 0:
                break

        for edge_id in reversed(path):
            self.add_flow(edge_id, min_cap)
        return min_cap < float('inf') and min_cap > 0

    def max_flow(self, from_, to):
        flow = 0
        exist_augmenting_path = True
        while exist_augmenting_path:
            prev = self.bfs(from_, to)
            if prev is None or to not in prev:
                break
            exist_augmenting_path = self.recalculate_flow(to, prev)

        edges_next_to_from_ = self.get_ids(from_)
        for edge_id in edges_next_to_from_:
            current = self.get_edge(edge_id)
            if current.capacity > 0:
                flow += current.flow
        return flow


if __name__ == '__main__':
    graph = FlowGraph()
    graph.read_data()
    print(graph.max_flow(0, graph.size() - 1))
