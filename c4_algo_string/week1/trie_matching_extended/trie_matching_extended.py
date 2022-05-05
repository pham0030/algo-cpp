# python3
import sys

# The trie built from patterns
# in the form of a dictionary of dictionaries,
# e.g. {0:{'A':1,'T':2},1:{'C':3}}
# where the key of the external dictionary is
# the node ID (integer), and the internal dictionary
# contains all the trie edges outgoing from the corresponding
# node, and the keys are the letters on those edges, and the
# values are the node IDs to which these edges lead.

# To make the code handle when one of the patterns is a prefix
# of another atter, end all the pattern with $


def build_trie(patterns):
    trie = dict()
    trie[0] = {}
    node_index = 1

    for pattern in patterns:
        pattern = pattern + '$'
        current_node = trie[0]
        for current_char in pattern:
            if current_char in current_node.keys():
                current_node = trie[current_node[current_char]]  # move along
            else:
                trie[node_index] = {}  # add node
                current_node[current_char] = node_index  # add edge
                current_node = trie[node_index]  # move to just created node
                node_index += 1

    return trie


def prefix_trie_matching(text, trie):
    node_idx = 0
    symbol = text[node_idx]
    v = trie[node_idx]

    while True:
        if not v or '$' in v.keys():
            return True
        elif symbol in v.keys():
            v = trie[v[symbol]]
            node_idx += 1
            symbol = text[node_idx] if node_idx < len(text) else None
        else:
            return False


def tree_matching(text, trie):
    result = []
    for i in range(len(text)):
        if prefix_trie_matching(text[i:], trie):
            result.append(i)
    return result

if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    n = int(sys.stdin.readline().strip())
    patterns = []
    for i in range(n):
        patterns += [sys.stdin.readline().strip()]

    trie = build_trie(patterns)
    ans = tree_matching(text, trie)

    sys.stdout.write(' '.join(map(str, ans)) + '\n')
