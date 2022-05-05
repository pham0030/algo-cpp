# python3

import sys
import random


class Node:
    def __init__(self, char, y, left, right):
        self.size = 1
        self.char, self.y, self.left, self.right = char, y, left, right

    def update(self):
        self.size = self.left.size + self.right.size + 1

    @staticmethod
    def init():
        node = Node(0, 0, None, None)
        node.size = 0
        Node.nul = node.left = node.right = node
        Node.cnt = 0
Node.init()


class Rope:  # simple tree no splay operation with random initialization

    @staticmethod
    def merge(m, n):  # recursively merge two nodes m and n
        if m == Node.nul:
            return n
        if n == Node.nul:
            return m
        if m.y < n.y:
            m.right = Rope.merge(m.right, n)
            m.update()
            return m
        else:
            n.left = Rope.merge(m, n.left)
            n.update()
            return n

    @staticmethod
    def split(tree, key):  # recursively split tree; input: tree root and key
        if tree == Node.nul:
            return (Node.nul, Node.nul)
        if tree.left.size < key:
            (left_sub, right_sub) = Rope.split(tree.right,
                                               key - tree.left.size - 1)
            tree.right = left_sub
            tree.update()
            return(tree, right_sub)
        else:
            (left_sub, right_sub) = Rope.split(tree.left, key)
            tree.left = right_sub
            tree.update()
            return(left_sub, tree)

    @staticmethod
    def print_out(tree, buffer):  # in order traverse print out
        if tree == Node.nul:
            return
        Rope.print_out(tree.left, buffer)
        buffer.append(tree.char)
        Rope.print_out(tree.right, buffer)

    def __init__(self, string):
        self.root = Node.nul
        for char in string:
            new_node = Node(char,
                            random.randint(0, 1 << 30), Node.nul, Node.nul)
            self.root = Rope.merge(self.root, new_node)

    def result(self):
        buffer = []
        Rope.print_out(self.root, buffer)
        return "".join(buffer)

    def process(self, i, j, k):
        j += 1
        # slice the section
        left, right = Rope.split(self.root, i)
        middle, right = Rope.split(right, j - i)
        # merge the remaining and slice for insertion
        left, right = Rope.split(Rope.merge(left, right), k)
        # insertion
        self.root = Rope.merge(Rope.merge(left, middle), right)


rope = Rope(sys.stdin.readline().strip())
q = int(sys.stdin.readline())
for _ in range(q):
    i, j, k = map(int, sys.stdin.readline().strip().split())
    rope.process(i, j, k)
print(rope.result())
