# python3
import sys
import threading
sys.setrecursionlimit(10**6)  # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size


class Node:
    def __init__(self, leading_to_edge):
        self.leading_to_edge = leading_to_edge  # label on edge leading to node
        self.out = {}  # outgoing edges map character to nodes


class SuffixTree:

    def __init__(self, text):
        self.root = Node(None)
        self.root.out[text[0]] = Node(text)  # initialize tree for full text
        for i in range(1, len(text)):  # iterate over all suffix of text
            # start at root with first char of suffix
            current_node = self.root
            j = i
            while j < len(text):

                # at a node if char of suffix is mapped to other node,
                # start walking down that path
                if text[j] in current_node.out.keys():
                    child_node = current_node.out[text[j]]
                    edge_label = child_node.leading_to_edge

                    # walk down the path until we reach the child node
                    # or there is a mismatch between edge label and suffix
                    k = j + 1
                    while k - j < len(edge_label) and \
                            text[k] == edge_label[k - j]:
                        k += 1

                    # if we reached the child node go to outer loop to
                    # check if there is new path
                    if k - j == len(edge_label):
                        current_node = child_node
                        j = k
                    else:  # there is a mismatch at the middle of the edge
                        # create a mid node to cut the edge
                        mid_node = Node(edge_label[:k-j])
                        # create a new end node and edge from mid node
                        mid_node.out[text[k]] = Node(text[k:])
                        # connect mid node to original parent
                        current_node.out[text[j]] = mid_node
                        # connect mid node to original child
                        mid_node.out[edge_label[k-j]] = child_node
                        # adjust original child leading edge label
                        child_node.leading_to_edge = edge_label[k-j:]

                # at a node if char of suffix is not mapped to any other node,
                # there is no path to follow so make new edge and node from
                # the current node
                else:
                    current_node.out[text[j]] = Node(text[j:])


def print_all_edges(tree):

    def recursive_traverse(node):
        for child_node in node.out:
            print(node.out[child_node].leading_to_edge)
            recursive_traverse(node.out[child_node])

    recursive_traverse(tree.root)


def main():
    text = sys.stdin.readline().strip()
    tree = SuffixTree(text)
    print_all_edges(tree)


threading.Thread(target=main).start()
