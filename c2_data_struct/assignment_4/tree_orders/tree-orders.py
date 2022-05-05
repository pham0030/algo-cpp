# python3


import sys
import threading
sys.setrecursionlimit(10**6)  # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size


class TreeOrders:
    def read(self):
        self.n = int(sys.stdin.readline())
        self.key = [0 for i in range(self.n)]
        self.left = [0 for i in range(self.n)]
        self.right = [0 for i in range(self.n)]
        for i in range(self.n):
            [a, b, c] = map(int, sys.stdin.readline().split())
            self.key[i] = a
            self.left[i] = b
            self.right[i] = c

    def in_order(self):
        self.result = []

        def recursive(node):
            if self.left[node] != -1:
                recursive(self.left[node])
            self.result.append(self.key[node])
            if self.right[node] != -1:
                recursive(self.right[node])
        recursive(0)

        return self.result

    def pre_order(self):
        self.result = []

        def recursive(node):
            self.result.append(self.key[node])
            if self.left[node] != -1:
                recursive(self.left[node])
            if self.right[node] != -1:
                recursive(self.right[node])
        recursive(0)

        return self.result

    def post_order(self):
        self.result = []

        def recursive(node):
            if self.left[node] != -1:
                recursive(self.left[node])
            if self.right[node] != -1:
                recursive(self.right[node])
            self.result.append(self.key[node])
        recursive(0)

        return self.result


def main():
    tree = TreeOrders()
    tree.read()
    print(" ".join(str(x) for x in tree.in_order()))
    print(" ".join(str(x) for x in tree.pre_order()))
    print(" ".join(str(x) for x in tree.post_order()))

threading.Thread(target=main).start()
