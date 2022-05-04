# python3
import sys


class TreeNode:

    def __init__(self, id, parent, children, depth, start, end):
        self.id = id
        self.parent = parent  # connect by int id
        self.children = children  # connect by int id
        self.depth = depth
        self.start = start
        self.end = end


def create_new_leaf(tree, parent, text, suffix):
    leaf = TreeNode(len(tree), parent.id, {},
                    len(text)-suffix, suffix+parent.depth, len(text)-1)
    tree[leaf.id] = leaf
    parent.children[text[leaf.start]] = leaf.id


def break_edge(tree, node, text, start, offset):
    start_char = text[start]
    mid_char = text[start+offset]
    # create new mid node:
    mid_node = TreeNode(len(tree), node.id, {}, node.depth+offset,
                        start, start+offset-1)
    tree[mid_node.id] = mid_node  # add the mid_node to the tree

    # adjust the edge of the original child to correct start position
    tree[node.children[start_char]].start += offset

    # set original child of node to be child of mid_node:
    mid_node.children[mid_char] = node.children[start_char]
    tree[node.children[start_char]].parent = mid_node.id  # reset its parent

    # connect the node to mid_node:
    node.children[start_char] = mid_node.id  # also remove original child
    return mid_node


def suffix_array_to_suffix_tree(suffix_array, lcp_array, text):
    """
    Build suffix tree of the string text given its suffix array suffix_array
    and LCP array lcp_array. Return the tree as a mapping from a node ID
    to the list of all outgoing edges of the corresponding node. The edges in
    the list must be sorted in the ascending order by the first character of
    the edge label. Root must have node ID = 0, and all other node IDs
    must be different nonnegative integers.
    Each edge must be represented by a tuple (node, start, end), where
        * node is the node ID of the ending node of the edge
        * start is the starting position (0-based) of the substring of
          text corresponding to the edge label
        * end is the first position (0-based) after the end of the
          substring corresponding to the edge label
    For example, if text = "ACACAA$", an edge with label "$" from root to
    a node with ID 1 must be represented by a tuple (1, 6, 7).
    This edge must be present in the list tree[0]
    (corresponding to the root node), and it should be the first edge in the
    list (because it has the smallest first character of all edges outgoing
    from the root).
    """
    tree = {}

    node_tree = {}
    root = TreeNode(len(node_tree), None, {}, 0, None, None)
    node_tree[root.id] = root
    lcp_prev = 0
    current_node = root

    for i in range(len(text)):
        suffix = suffix_array[i]

        # move up the tree from the current node as long as
        # we hit the lcp then we stop
        while current_node.depth > lcp_prev:
            current_node = node_tree[current_node.parent]

        # if we stop exactly at a node, create new leaf from that node
        if current_node.depth == lcp_prev:
            create_new_leaf(node_tree, current_node, text, suffix)
        # else if we stop in the middle of an edge, break that edge and
        # create a new mid node
        else:
            # new edge start
            edge_start = suffix_array[i-1] + current_node.depth
            offset = lcp_prev - current_node.depth
            mid_node = break_edge(node_tree, current_node, text,
                                  edge_start, offset)
            create_new_leaf(node_tree, mid_node, text, suffix)
            current_node = mid_node
        if i < len(text) - 1:
            lcp_prev = lcp_array[i]

    # node_tree completed, however needed to converted to tree with edges
    # with suggested format output for printing purpose
    for i in range(len(node_tree)):
        current = node_tree[i]  # getting the current node
        if current.children:
            neighbours = []
            for c in current.children:
                child = node_tree[current.children[c]]
                neighbours.append((child.id, child.start, child.end+1))
            neighbours.sort()  # sorting wrt id for printing in ascending order
            tree[current.id] = neighbours

    return tree

if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    sa = list(map(int, sys.stdin.readline().strip().split()))
    lcp = list(map(int, sys.stdin.readline().strip().split()))
    print(text)
    # Build the suffix tree and get a mapping from
    # suffix tree node ID to the list of outgoing Edges.
    tree = suffix_array_to_suffix_tree(sa, lcp, text)
    """
    Output the edges of the suffix tree in the required order.
    Note that we use here the contract that the root of the tree
    will have node ID = 0 and that each vector of outgoing edges
    will be sorted by the first character of the corresponding edge label.

    The following code avoids recursion to avoid stack overflow issues.
    It uses two stacks to convert recursive function to a while loop.
    This code is an equivalent of

        OutputEdges(tree, 0);

    for the following _recursive_ function OutputEdges:

    def OutputEdges(tree, node_id):
        edges = tree[node_id]
        for edge in edges:
            print("%d %d" % (edge[1], edge[2]))
            OutputEdges(tree, edge[0]);

    """
    stack = [(0, 0)]
    result_edges = []
    while len(stack) > 0:
        (node, edge_index) = stack[-1]
        stack.pop()
        if node not in tree:
            continue
        edges = tree[node]
        if edge_index + 1 < len(edges):
            stack.append((node, edge_index + 1))
        print("%d %d" % (edges[edge_index][1], edges[edge_index][2]))
        stack.append((edges[edge_index][0], 0))
