# python3
import sys

# Return the trie built from patterns
# in the form of a dictionary of dictionaries,
# e.g. {0:{'A':1,'T':2},1:{'C':3}}
# where the key of the external dictionary is
# the node ID (integer), and the internal dictionary
# contains all the trie edges outgoing from the corresponding
# node, and the keys are the letters on those edges, and the
# values are the node IDs to which these edges lead.


def build_trie(patterns):
    tree = dict()
    tree[0] = {}
    node_index = 1

    for pattern in patterns:
        current_node = tree[0]
        for current_char in pattern:
            if current_char in current_node.keys():
                current_node = tree[current_node[current_char]]  # move along
            else:
                tree[node_index] = {}  # add node
                current_node[current_char] = node_index  # add edge
                current_node = tree[node_index]  # move to just created node
                node_index += 1

    return tree


if __name__ == '__main__':
    patterns = sys.stdin.read().split()[1:]
    tree = build_trie(patterns)
    for node in tree:
        for c in tree[node]:
            print("{}->{}:{}".format(node, tree[node][c], c))
