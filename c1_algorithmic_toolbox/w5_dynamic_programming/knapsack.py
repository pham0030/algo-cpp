# Uses python3
import sys
import time
import random


def optimal_weight(W, w):
    n = len(w)
    value_matrix = [[0 for j in range(W+1)] for i in range(n+1)]
    # print(value_matrix)
    for i in range(1, n+1):
        for w_ in range(1, W+1):
            value_matrix[i][w_] = value_matrix[i-1][w_]
            if w[i-1] <= w_:
                val = value_matrix[i-1][w_-w[i-1]] + w[i-1]
                if value_matrix[i][w_] < val:
                    value_matrix[i][w_] = val
    # print(value_matrix)
    return value_matrix[n][W]

if __name__ == '__main__':
    input_ = sys.stdin.read()
    W, n, *w = list(map(int, input_.split()))
    print(optimal_weight(W, w))

    # with open('input.txt') as f:
    #     input_ = f.read()
    #     W, n, *w = list(map(int, input_.split()))
    #     print(optimal_weight(W, w))

    # Debug test
    # random.seed(1)
    # # W = random.randint(1, int(1e4))
    # # n = random.randint(1, 300)
    # W = int(1e4)
    # n = 300
    # w = [random.randint(1, int(1e5)) for _ in range(n)]

    # t0 = time.time()
    # print(optimal_weight(W, w))
    # t0 = time.time() - t0
    # print('Running time: {}'.format(t0))
