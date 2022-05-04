# python3

import sys
import threading

sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size


def IsBinarySearchTree(tree):

    def is_bst(node, min, max):
        key = node[0]
        if key < min:
            return False
        if key >= max:
            return False
        left_is_bst = True
        right_is_bst = True
        left = node[1]
        if left != -1:
            left_is_bst = is_bst(tree[left], min, key)
        right = node[2]
        if right != -1:
            right_is_bst = is_bst(tree[right], key, max)
        return left_is_bst and right_is_bst
    if tree == []:
        return True

    return is_bst(tree[0], float('-inf'), float('inf'))


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
