# python3

import sys
import threading

sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size


def IsBinarySearchTree(tree):
    # Implement correct algorithm here
    ans = True
    if tree == []:
        return ans

    prev = float('-inf')

    def is_bst(node):
        nonlocal ans
        nonlocal prev

        left = node[1]
        if left != -1:
            ans = is_bst(tree[left])

        key = node[0]

        if key <= prev:
            ans = False
        prev = key
        right = node[2]
        if right != -1:
            ans = is_bst(tree[right])
        return ans

    return is_bst(tree[0])


def main():
    nodes = int(sys.stdin.readline().strip())
    tree = []
    for i in range(nodes):
        tree.append(list(map(int, sys.stdin.readline().strip().split())))
    if IsBinarySearchTree(tree):
        print("CORRECT")
    else:
        print("INCORRECT")

threading.Thread(target=main).start()
