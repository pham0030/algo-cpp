# python3
import sys
import threading

sys.setrecursionlimit(10**6)  # max depth of recursion
threading.stack_size(2**26)  # new thread will get stack of such size


class TwoSATSolver:

    def __init__(self):
        self.num_vars = None
        self.num_clauses = None
        self.implication_graph = None
        self.implication_graph_reversed = None
        self.sccs = None
        self.order = None
        self.visisted = None
        self.result = None

    """
    Implication graphs structures:
    self.implication_graph:
    i-th list contains outgoing nodes of node i-th
    for example: node 0 directs to nodes 1, 2, 5: 0->1, 0->2, 0->5
                 self.implication_graph[0] = [1, 2, 5]
    self.implication_graph_reversed:
    i-th list contains incoming nodes of node i-th
    for example: node 1 directed by nodes 0, 2: 1<-0, 1<-2
                 self.implication_graph_reversed[1] = [0, 2]

    Number of implication graph nodes = 2*number of variables, eg:
    Variables x1, x2, x3 and their negation -x1, -x2, -x3:
    Node ID   0   1    2                      3    4    5
    for i in range(2*self.num_vars):
        self.implication_graph[i] = set()
        self.implication_graph_reversed[i] = set()
    """

    def read_data_console(self):
        self.num_vars, self.num_clauses = map(int, input().split())

        # Reading data and building implication graph concurrently
        # to save time
        self.implication_graph = [[] for _ in range(2*self.num_vars)]
        self.implication_graph_reversed = [[] for _
                                           in range(2*self.num_vars)]
        for i in range(self.num_clauses):
            clause = list(map(int, input().split()))
            if clause[0] > 0:
                l1 = clause[0] - 1
                not_l1 = l1 + self.num_vars
            else:
                l1 = -clause[0] + self.num_vars - 1
                not_l1 = l1 - self.num_vars
            if clause[1] > 0:
                l2 = clause[1]-1
                not_l2 = l2 + self.num_vars
            else:
                l2 = -clause[1] + self.num_vars - 1
                not_l2 = l2 - self.num_vars
            self.implication_graph[not_l1].append(l2)
            self.implication_graph[not_l2].append(l1)
            self.implication_graph_reversed[l2].append(not_l1)
            self.implication_graph_reversed[l1].append(not_l2)

    def read_data_file(self, file_path):
        with open(file_path, 'r') as f:
            self.num_vars, self.num_clauses = map(int, f.readline().split())

            # Reading data and building implication graph concurrently
            # to save time
            self.implication_graph = [[] for _ in range(2*self.num_vars)]
            self.implication_graph_reversed = [[] for _
                                               in range(2*self.num_vars)]
            for i in range(self.num_clauses):
                clause = list(map(int, f.readline().split()))
                if clause[0] > 0:
                    l1 = clause[0] - 1
                    not_l1 = l1 + self.num_vars
                else:
                    l1 = -clause[0] + self.num_vars - 1
                    not_l1 = l1 - self.num_vars
                if clause[1] > 0:
                    l2 = clause[1]-1
                    not_l2 = l2 + self.num_vars
                else:
                    l2 = -clause[1] + self.num_vars - 1
                    not_l2 = l2 - self.num_vars
                self.implication_graph[not_l1].append(l2)
                self.implication_graph[not_l2].append(l1)
                self.implication_graph_reversed[l2].append(not_l1)
                self.implication_graph_reversed[l1].append(not_l2)

    def find_strongly_connected_components(self):
        # first depth first search to find topological order
        # from implication graph reversed
        self.order = []
        self.visisted = [False for _ in range(2*self.num_vars)]
        for i in range(2*self.num_vars):
            if not self.visisted[i]:
                self.visisted[i] = True
                self.dfs1(i)
                self.order.append(i)

        # second depth first search to find strongly connected
        # components
        self.visisted = [False for _ in range(2*self.num_vars)]
        self.sccs = []
        for x in reversed(self.order):
            if not self.visisted[x]:
                # CRITICALLY IMPORTANT for efficiency need to use set()
                # for strongly connected component group (scc).
                # Dont use list() because it is very slow
                scc = set()
                # scc = []
                self.visisted[x] = True
                self.dfs2(x, scc)
                self.sccs.append(scc)

    def dfs1(self, x):
        for next_x in self.implication_graph_reversed[x]:
            if not self.visisted[next_x]:
                self.visisted[next_x] = True
                self.dfs1(next_x)
                self.order.append(next_x)

    def dfs2(self, x, scc):
        scc.add(x)
        # scc.append(x)
        for next_x in self.implication_graph[x]:
            if not self.visisted[next_x]:
                self.visisted[next_x] = True
                self.dfs2(next_x, scc)

    def solve_2sat(self):
        self.result = [None for _ in range(self.num_vars)]
        if self.is_satisfiable():
            print("SATISFIABLE")
            for i in range(1, self.num_vars+1):
                if self.result[i-1] == 1:
                    print(-i, end="")
                else:
                    print(i, end="")
                if i < self.num_vars:
                    print(" ", end="")
                else:
                    print()
        else:
            print("UNSATISFIABLE")
        pass

    def is_satisfiable(self):
        for scc in self.sccs:
            for x in scc:
                # if x and not x are in the same scc then False
                # if scc is list(), this if statement will be very slow
                # use scc with set() for efficiency
                if (x+self.num_vars) in scc or (x-self.num_vars) in scc:
                    return False
        for scc in self.sccs:
            for i in scc:
                is_negative = False
                if i >= self.num_vars:
                    x = i-self.num_vars
                    is_negative = True
                else:
                    x = i
                    is_negative = False
                if self.result[x] is None:
                    if is_negative:
                        self.result[x] = 1
                    else:
                        self.result[x] = 0
        return True


def main():
    # Testing purpose
    # import os
    # import time
    # cwd = os.getcwd()
    # file_name = "V100k.case"
    # full_path = os.path.join(cwd, file_name)

    # t0 = time.time()
    # circuit_design = TwoSATSolver()

    # t1 = time.time()
    # circuit_design.read_data_file(full_path)
    # t1 -= time.time()

    # t2 = time.time()
    # circuit_design.find_strongly_connected_components()
    # t2 -= time.time()

    # t3 = time.time()
    # circuit_design.solve_2sat()
    # t3 -= time.time()

    # t0 -= time.time()
    # print('t1 %: ', t1/t0*100)
    # print('t2 %: ', t2/t0*100)
    # print('t3 %: ', t3/t0*100)
    # print('t0:', -t0)
    # print(circuit_design.num_vars)
    # print(circuit_design.num_clauses)

    # For uploading
    circuit_design = TwoSATSolver()
    circuit_design.read_data_console()
    circuit_design.find_strongly_connected_components()
    circuit_design.solve_2sat()

threading.Thread(target=main).start()
