# python3
import sys


def preprocess_BWT(bwt):
    """
    Preprocess the Burrows-Wheeler Transform bwt of some text
    and compute as a result:
        * starts - for each character C in bwt, starts[C] is the
            first position of this character in the sorted array of
            all characters of the text.
        * occ_counts_before - for each character C in bwt and each position P
            in bwt, occ_count_before[C][P] is the number of occurrences
            of character C in bwt from position 0 to position P inclusive.
    """
    first_column = "".join(sorted(bwt))
    characters = set(first_column)
    starts = {char: first_column.find(char) for char in characters}

    occ_counts_before = {}
    for char in characters:
        counter = 0
        column = [0]
        for i in range(len(bwt)):
            if bwt[i] == char:
                counter += 1
            column.append(counter)
        occ_counts_before[char] = column

    return starts, occ_counts_before


def count_occurrences(pattern, bwt, starts, occ_counts_before):
    """
    Compute the number of occurrences of string pattern in the text
    given only Burrows-Wheeler Transform bwt of the text and additional
    information we get from the preprocessing stage - starts and
    occ_counts_before.
    """
    top, bottom = 0, len(bwt) - 1
    pattern = list(pattern)
    while top <= bottom:
        if pattern:
            char = pattern.pop()
            if char in bwt[top:bottom+1]:
                top = starts[char] + occ_counts_before[char][top]
                bottom = starts[char] + occ_counts_before[char][bottom+1] - 1
            else:
                return 0
        else:
            return bottom - top + 1


if __name__ == '__main__':
    bwt = sys.stdin.readline().strip()
    pattern_count = int(sys.stdin.readline().strip())
    patterns = sys.stdin.readline().strip().split()
    # Preprocess the BWT once to get starts and occ_count_before.
    # For each pattern, we will then use these precomputed values and
    # spend only O(|pattern|) to find all occurrences of the pattern
    # in the text instead of O(|pattern| + |text|).
    starts, occ_counts_before = preprocess_BWT(bwt)
    occurrence_counts = []
    for pattern in patterns:
        occurrence_counts.append(count_occurrences(pattern, bwt, starts,
                                                   occ_counts_before))
    print(' '.join(map(str, occurrence_counts)))
