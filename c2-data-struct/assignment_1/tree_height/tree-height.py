# python3

import sys
import threading
import os
import time
import psutil
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size


class TreeHeightNaive:
    def read(self):
        self.n = int(sys.stdin.readline())
        self.parent = list(map(int, sys.stdin.readline().split()))

    def compute_height(self):
        maxHeight = 0
        for vertex in range(self.n):
            height = 0
            i = vertex
            while i != -1:
                height += 1
                i = self.parent[i]
            maxHeight = max(maxHeight, height)
        return maxHeight


class Node:
    def __init__(self):
        self.child_indexes = []
        self.parent_index = -1

    def add_child(self, child_index):
        self.child_indexes.append(child_index)

    def set_parent(self, parent_index):
        self.parent_index = parent_index


class Tree:
    def __init__(self, n=None, parent=None):
        self.n = n
        self.parent = parent

    def read(self):
        self.n = int(sys.stdin.readline())
        self.parent = list(map(int, sys.stdin.readline().split()))

    def build_tree(self):
        self.nodes = [Node() for i in range(self.n)]
        self.level = [None for i in range(self.n)]
        # Building the tree
        for index in range(self.n):
            parent_index = self.parent[index]
            if parent_index == -1:
                self.root = index
            else:
                self.nodes[parent_index].add_child(index)
                self.nodes[index].set_parent(parent_index)
        # Compute the tree height
        for i in range(self.n):
            self.compute_level(i)
        self.height = max(self.level)

    def compute_level(self, idx):  # Recursive approach
        if idx == self.root:
            self.level[idx] = 1
            return self.level[idx]
        if self.level[idx] is not None:
            return self.level[idx]
        else:
            self.level[idx] = self.compute_level(
                self.nodes[idx].parent_index) + 1
            return self.level[idx]


def main():
    # tree = Tree()
    # tree.read()
    # tree.build_tree()
    # print(tree.height)

    # Testing all cases:
    time_limit = 5.0  # seconds
    max_time_used = 0.0  # seconds
    memory_limit = 512  # MB
    max_memory_used = 0  # MB
    cwd = os.getcwd()
    cases = ['01', '02', '03', '04', '05', '06', '07', '08', '09']
    for i in range(10, 25):
        cases.append(str(i))

    for c in cases:
        print('-'*20)
        print('Test case: {}'.format(c))
        text_path = os.path.join(cwd, 'tree_height/tests/', c)
        # print(text_path)
        with open(text_path) as t:
            n = int(t.readline())
            parent = list(map(int, t.readline().split()))
            # print(n)
            # print(parent)

        result_path = text_path + '.a'
        with open(result_path) as crf:
            cr = int(crf.read())

        t0 = time.time()
        tree = Tree()
        tree.n = n
        tree.parent = parent
        tree.build_tree()
        r = tree.height
        t = time.time() - t0
        if t > max_time_used:
            max_time_used = t

        process = psutil.Process(os.getpid())
        m = process.memory_info().rss/(1024**2)
        if m > max_memory_used:
            max_memory_used = m
        if r != cr:
            print('Wrong!')
            print('Your output: {}'.format(r))
            print('Correct output: {}'.format(cr))
            break
        elif max_time_used > time_limit:
            print('Too slow!')
            print('Running time: {}'.format(t))
            break
        elif max_memory_used > memory_limit:
            print('Too much memory!')
            print('Memory used: {}MB'.format(max_memory_used))
        else:
            print('Passed')
        # input("\n\tpaused: press Enter to continue\n")
        print('Memory used: {0:.2f} MB'.format(m))
        # print('Running time: {}'.format(t))
    print('-'*20)
    print('Max time used: {0:.2f} s'.format(max_time_used))
    print('Max memory used: {0:.2f} MB'.format(max_memory_used))

threading.Thread(target=main).start()
