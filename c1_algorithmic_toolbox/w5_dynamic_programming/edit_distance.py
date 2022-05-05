# Uses python3
import random


def edit_distance(A, B):
    n = len(A)
    m = len(B)
    D = [[0 for j in range(m + 1)] for i in range(n + 1)]
    for i in range(n+1):
        D[i][0] = i
    for j in range(m+1):
        D[0][j] = j

    for j in range(1, m+1):
        for i in range(1, n+1):
            insertion = D[i][j-1] + 1
            deletion = D[i-1][j] + 1
            match = D[i-1][j-1]
            mismatch = D[i-1][j-1] + 1
            if A[i-1] == B[j-1]:
                D[i][j] = min(insertion, deletion, match)
            else:
                D[i][j] = min(insertion, deletion, mismatch)

    # # Print Distance Matrix D
    # for i in range(n+1):
    #     for j in range(m+1):
    #         print('{0:4}'.format(D[i][j]), end=' ')
    #     print()

    return D[n][m]

if __name__ == "__main__":
    print(edit_distance(input(), input()))

    # # Time test
    # alphabet = u'0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    # A = [random.choice(alphabet) for i in range(100)]
    # B = [random.choice(alphabet) for i in range(100)]
    # print(edit_distance(A, B))
