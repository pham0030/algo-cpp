# python3


class Edge:

    def __init__(self):
        self.from_ = None
        self.to_ = None


class ColorGraph:

    def __init__(self):
        self.num_nodes = None
        self.num_edges = None
        self.edges = None
        self.num_clauses = None
        self.num_vars = None

    def read_data(self):
        self.num_nodes, self.num_edges = map(int, input().split())
        edges = [list(map(int, input().split()))
                 for _ in range(self.num_edges)]

        self.edges = []
        for i in range(self.num_edges):
            edge = Edge()
            edge.from_, edge.to_ = edges[i][0], edges[i][1]
            self.edges.append(edge)

    def print_equisatisfiable_sat_formula(self):
        """
         For each node there is 3 variables for each color (num colors = 3)
         For example, for a graph with three nodes, the variables are:
         1(node 1, color 1)
         2(node 2, color 1)
         3(node 3, color 1)
         4(node 1, color 2)
         5(node 2, color 2)
         6(node 3, color 2)
         7(node 1, color 3)
         8(node 2, color 3)
         9(node 3, color 3)
         Condition:
         a) Node can only be coloured by one color at a time,
            for example node 1
            1 or 4 or 9
         b) Two nodes connected can only colored by different color,
            for example edge with node1-node2:
            (not 1) or (not 2) <- for first color
            (not 4) or (not 5) <- for second color
            (not 7) or (not 8) <- for third color
        """
        self.num_clauses = self.num_nodes+self.num_edges*3
        self.num_vars = self.num_nodes*3
        print("{} {}".format(self.num_clauses, self.num_vars))

        # Node can only be colored by one color at a time
        for i in range(1, self.num_nodes+1):
            print("{} {} {} 0".format(i, i+self.num_nodes, i+2*self.num_nodes))
        # Two nodes connected can only be colored by different color
        for edge in self.edges:
            print("{} {} 0".format(-edge.from_, -edge.to_))
            print("{} {} 0".format(-edge.from_-self.num_nodes,
                                   -edge.to_-self.num_nodes))
            print("{} {} 0".format(-edge.from_-self.num_nodes*2,
                                   -edge.to_-self.num_nodes*2))


if __name__ == "__main__":
    network = ColorGraph()
    network.read_data()
    network.print_equisatisfiable_sat_formula()
