# python3
import sys
"""
Considering charaters $, A, C, G and T only. Therefore
the total size of this alphabet is 5 only
"""


def sort_characters(S):
    len_S = len(S)
    order = [None] * len_S
    size_alphabet = 5  # $, A, C, G and T only
    to_idx = {'$': 0, 'A': 1, 'C': 2, 'G': 3, 'T': 4}
    count = [0] * size_alphabet
    try:
        for i in range(len_S):
            count[to_idx[S[i]]] += 1
        for j in range(1, size_alphabet):
            count[j] += count[j-1]

        for i in reversed(range(len_S)):
            char = S[i]
            count[to_idx[char]] -= 1
            order[count[to_idx[char]]] = i
        return order
    except KeyError as err:
        print(err)
        print("Only accept value: '$', 'A', 'C', 'G' and 'T'")
        return None


def compute_char_classes(S, order):
    len_S = len(S)
    char_classes = [None] * len_S
    char_classes[order[0]] = 0
    for i in range(1, len_S):
        if S[order[i]] != S[order[i-1]]:
            char_classes[order[i]] = char_classes[order[i-1]] + 1
        else:
            char_classes[order[i]] = char_classes[order[i-1]]
    return char_classes


def sort_doubled(S, L, order, char_classes):
    len_S = len(S)
    count = [0] * len_S
    new_order = [None] * len_S
    for i in range(len_S):
        count[char_classes[i]] += 1
    for j in range(1, len_S):
        count[j] += count[j-1]

    for i in reversed(range(len_S)):
        start = (order[i] - L + len_S) % len_S
        cl = char_classes[start]
        count[cl] -= 1
        new_order[count[cl]] = start
    return new_order


def update_classes(new_order, char_classes, L):
    n = len(new_order)
    new_classes = [None] * n
    new_classes[new_order[0]] = 0
    for i in range(1, n):
        cur, prev = new_order[i], new_order[i-1]
        mid_idx = (cur + L) % n
        mid_prev = (prev + L) % n
        if char_classes[cur] != char_classes[prev] or \
           char_classes[mid_idx] != char_classes[mid_prev]:
            new_classes[cur] = new_classes[prev] + 1
        else:
            new_classes[cur] = new_classes[prev]
    return new_classes


def build_suffix_array(text):
    """
    Build suffix array of the string text and
    return a list result of the same length as the text
    such that the value result[i] is the index (0-based)
    in text where the i-th lexicographically smallest
    suffix of text starts.
    """
    len_S = len(text)
    order = sort_characters(text)
    char_classes = compute_char_classes(text, order)
    L = 1
    while L < len_S:
        order = sort_doubled(text, L, order, char_classes)
        char_classes = update_classes(order, char_classes, L)
        L *= 2

    return order


# pattern matching with suffix array: binary search
def pattern_matching(text, pattern, suffix_array):
    len_text = len(text)
    len_pattern = len(pattern)
    min_idx = 0
    max_idx = len_text
    while min_idx < max_idx:
        mid_idx = (min_idx + max_idx)//2
        if pattern > text[suffix_array[mid_idx]:min(suffix_array[mid_idx] +
                                                    len_pattern, len_text)]:
            min_idx = mid_idx + 1
        else:
            max_idx = mid_idx
    start = min_idx
    max_idx = len_text
    while min_idx < max_idx:
        mid_idx = (min_idx + max_idx)//2
        if pattern < text[suffix_array[mid_idx]:min(suffix_array[mid_idx] +
                                                    len_pattern, len_text)]:
            max_idx = mid_idx
        else:
            min_idx = mid_idx + 1
    end = max_idx
    if start > end:
        return None
    else:
        return [suffix_array[i] for i in range(start, end)]


def print_occurrences(text, patterns):
    suffix_array = build_suffix_array(text)
    results = set()  # use set for efficient print
    for pattern in patterns:
        result = pattern_matching(text, pattern, suffix_array)
        if result:
            results |= set(result)  # union is much faster than list.append
    for ele in results:
        print(ele, end=' ')


if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    pattern_count = int(sys.stdin.readline().strip())
    patterns = sys.stdin.readline().strip().split()
    text += '$'
    print_occurrences(text, patterns)
