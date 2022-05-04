# python3


class Edge:

    def __init__(self):
        self.from_ = None
        self.to_ = None

"""
    Creating Hamiltonian Path clauses condition for SAT-solver
    For example the following path: with 3 nodes and 2 edges,
    3 2
    1 2
    2 3
    This  input format, corresspondint to graph presentation: 1 -> 2 -> 3
    This Hamiltonian path will have 3 positions (for each node),
    create a variable for each node at each position. For this graph:
    Node    1   2   3
    VarID   1   2   3   <- position 1
    VarID   4   5   6   <- position 2
    VarID   7   8   9   <- position 3
    Variables 1, 4, 7 represent the node 1 at position 1, 2, 3 respectively.
    Similarly for node 2 and 3
"""


class HamiltonianPath:

    def __init__(self):
        self.num_nodes = None
        self.num_edges = None
        self.edges = None
        self.num_clauses = None
        self.num_vars = None
        self.adj = None
        self.clauses = []

    def read_data(self):
        self.num_nodes, self.num_edges = map(int, input().split())
        edges = [list(map(int, input().split()))
                 for _ in range(self.num_edges)]

        self.edges = []
        for i in range(self.num_edges):
            edge = Edge()
            edge.from_, edge.to_ = edges[i][0], edges[i][1]
            self.edges.append(edge)

        # Forming adjacent matrix
        # True if there is an edge between nodes and False otherwise
        self.adj = [[False for _ in range(self.num_nodes)]
                    for _ in range(self.num_nodes)]
        for edge in self.edges:
            self.adj[edge.from_-1][edge.to_-1] = True
            self.adj[edge.to_-1][edge.from_-1] = True

    """
        Node    1   2   3
        VarID   1   2   3   <- position 1
        VarID   4   5   6   <- position 2
        VarID   7   8   9   <- position 3
        For example, condition for add exactly once of node 1 is as follow:
        (1 or 4 or 7) and (-1 or -4) and (-1 or -7) and (-4 or -7)
    """
    def add_exactly_once_node(self):
        for i in range(1, self.num_nodes+1):
            clause = [(i+j*self.num_nodes) for j in range(self.num_nodes)]
            self.clauses.append(clause)
            clauses = [[-i-j*self.num_nodes, -i-k*self.num_nodes]
                       for j in range(self.num_nodes-1)
                       for k in range(j+1, self.num_nodes)]
            self.clauses.extend(clauses)

    """
        Node    1   2   3
        VarID   1   2   3   <- position 1
        VarID   4   5   6   <- position 2
        VarID   7   8   9   <- position 3
        Graph 1 -> 2 -> 3
        For example: Node 1 is not connected to node 3 therefore
        the following conditions must hold False:
        1.Node 1 @ position 1 and Node 3 @ position 2: -1 or -6
        2.Node 3 @ position 1 and Node 1 @ position 2: -3 or -4
        3.Node 1 @ position 2 and Node 3 @ position 3: -4 or -9
        4.Node 3 @ position 2 and Node 1 @ position 3: -6 or -7
        5.Node 1 @ position 3 and Node 3 @ position 2: -7 or -6 (already have)
        6.Node 3 @ position 3 and Node 1 @ position 2: -9 or -4 (already have)
    """
    def add_graph_connectivity(self):
        for i in range(1, self.num_nodes):
            for j in range(i, self.num_nodes+1):
                if not self.adj[i-1][j-1] and i != j:
                    clauses = [[-i-k*self.num_nodes, -j-(k+1)*self.num_nodes]
                               for k in range(self.num_nodes-1)]
                    self.clauses.extend(clauses)
                    clauses = [[-j-k*self.num_nodes, -i-(k+1)*self.num_nodes]
                               for k in range(self.num_nodes-1)]
                    self.clauses.extend(clauses)

    """
        Node    1   2   3
        VarID   1   2   3   <- position 1
        VarID   4   5   6   <- position 2
        VarID   7   8   9   <- position 3
        Graph 1 -> 2 -> 3
        The following conditions will ensure that node 1, node 2, node 3
        cant take the same position 1
        (1 or 2 or 3) and (-1 or -2) and (-1 or -3) and( -2 or -3)
    """
    def nodes_cant_collide(self):
        for k in range(self.num_nodes):
            clause = [i+k*self.num_nodes for i in range(1, self.num_nodes+1)]
            self.clauses.append(clause)

            clauses = [[-i-k*self.num_nodes, -j-k*self.num_nodes]
                       for i in range(1, self.num_nodes)
                       for j in range(i+1, self.num_nodes+1)]
            self.clauses.extend(clauses)

    def print_equisatisfiable_sat_formula(self):
        self.add_exactly_once_node()
        self.add_graph_connectivity()
        self.nodes_cant_collide()
        print("{} {}".format(len(self.clauses), self.num_nodes**2))
        for c in self.clauses:
            for v in c:
                print("{}".format(v), end=" ")
            print("0")

if __name__ == "__main__":
    H_path = HamiltonianPath()
    H_path.read_data()
    H_path.print_equisatisfiable_sat_formula()
