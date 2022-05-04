# python3
import sys
import threading
sys.setrecursionlimit(10**6)  # max depth of recursion


class Node:
    def __init__(self, edge_label_start, edge_label_length, parent_node):
        # label on edge leading to node: start position and length on text
        self.edge_label_start = edge_label_start
        self.edge_label_length = edge_label_length
        self.childs = {}  # outgoing edges map a beginning character to nodes
        self.parent = parent_node


class SuffixTree:

    def __init__(self, text):
        # initialize tree for full text:
        self.text = text
        self.root = Node(None, None, None)
        self.root.childs[text[0]] = Node(0, len(text), self.root)
        for i in range(1, len(text)):  # iterate over all suffix of text
            # start at root with first char of suffix
            current_node = self.root
            j = i
            while j < len(text):

                # at a node if char of suffix is mapped to other node,
                # start walking down that path
                if text[j] in current_node.childs.keys():
                    child_node = current_node.childs[text[j]]
                    edge_label_start = child_node.edge_label_start
                    edge_label_length = child_node.edge_label_length

                    # walk down the path until we reach the childs node
                    # or there is a mismatch between edge label and suffix
                    k = j + 1
                    while k - j < edge_label_length and \
                            text[k] == text[edge_label_start + k - j]:
                        k += 1

                    # if we reached the childs node go to outer loop to
                    # check if there is new path
                    if k - j == edge_label_length:
                        current_node = child_node
                        j = k
                    else:  # there is a mismatch at the middle of the edge
                        # create a mid node to cut the edge
                        mid_node = Node(edge_label_start, k - j, current_node)
                        # connect mid node to original parent
                        current_node.childs[text[edge_label_start]] = mid_node

                        # create a new end node and edge from mid node
                        mid_node.childs[text[k]] = \
                            Node(k, len(text) - k, mid_node)
                        # connect mid node to original childs
                        mid_node.childs[text[edge_label_start + k - j]] = \
                            child_node
                        # adjust original childs leading edge label
                        child_node.parent = mid_node
                        child_node.edge_label_start = edge_label_start + k - j
                        child_node.edge_label_length -= (k - j)
                # at a node if char of suffix is not mapped to any other node,
                # there is no path to follow so make new edge and node from
                # the current node
                else:
                    current_node.childs[text[j]] = \
                        Node(j, len(text) - j, current_node)

    def print_all_edges(self):

        def recursive_traverse(node):
            for child_node in node.childs:
                i = node.childs[child_node].edge_label_start
                l = node.childs[child_node].edge_label_length
                print(self.text[i:i+l])
                recursive_traverse(node.childs[child_node])

        recursive_traverse(self.root)


text = sys.stdin.readline().strip()
tree = SuffixTree(text)
tree.print_all_edges()
