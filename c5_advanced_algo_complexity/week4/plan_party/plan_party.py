# python3


import sys
import threading

# This code is used to avoid stack overflow issues
sys.setrecursionlimit(10**6)  # max depth of recursion
threading.stack_size(2**26)  # new thread will get stack of such size


class Vertex:
    def __init__(self, weight):
        self.weight = weight
        self.children = []
        self.max_weight = 0


class Tree:
    def __init__(self):
        self.size = None
        self.tree = None

    def read_data_console(self):
        self.size = int(sys.stdin.readline())
        self.tree = [Vertex(w) for w in map(int, sys.stdin.readline().split())]
        for i in range(1, self.size):
            a, b = list(map(int, sys.stdin.readline().split()))
            self.tree[a - 1].children.append(b - 1)
            self.tree[b - 1].children.append(a - 1)

    def read_data_file(self, file_path):
        with open(file_path, 'r') as f:
            self.size = int(f.readline())
            self.tree = [Vertex(w) for w in map(int, f.readline().split())]
            for i in range(1, self.size):
                a, b = list(map(int, f.readline().split()))
                self.tree[a - 1].children.append(b - 1)
                self.tree[b - 1].children.append(a - 1)

    def max_weight_independent_tree_subset(self):
        # size = len(self.tree)
        if self.size == 0:
            return 0
        self.dfs(0, -1)  # begin to search at the root
        # You must decide what to return.
        return self.tree[0].max_weight

    # depth-first search.
    def dfs(self, vertex, parent):
        for child in self.tree[vertex].children:
            if child != parent:
                self.dfs(child, vertex)
        m1 = self.tree[vertex].weight
        m2 = 0
        for child in self.tree[vertex].children:
            if child != parent:
                m2 += self.tree[child].max_weight
                for grandchild in self.tree[child].children:
                    if grandchild != child and grandchild != parent:
                        m1 += self.tree[grandchild].max_weight
        self.tree[vertex].max_weight = max(m1, m2)


def main():

    # import os
    # file_name = '3'
    # cwd = os.getcwd()
    # full_path = os.path.join(cwd, file_name)

    # tree = Tree()
    # tree.read_data_file(full_path)
    # max_weight = tree.max_weight_independent_tree_subset()
    # print(max_weight)

    tree = Tree()
    tree.read_data_console()
    max_weight = tree.max_weight_independent_tree_subset()
    print(max_weight)

# This is to avoid stack overflow issues
threading.Thread(target=main).start()
