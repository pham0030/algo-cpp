# Uses python3
import sys
import time
import functools


def optimal_sequence(n):
    sequence = [[0], [1]]
    for i in range(2, n+1):
        temp = sequence[i-1][:]
        temp.append(i)
        sequence.extend([temp])
        if i % 3 == 0:
            j = i//3
            if len(sequence[j]) < len(sequence[i]) - 1:
                temp = sequence[j][:]
                temp.append(i)
                sequence[i] = temp
        if i % 2 == 0:
            j = i//2
            if len(sequence[j]) < len(sequence[i]) - 1:
                temp = sequence[j][:]
                temp.append(i)
                sequence[i] = temp
    return sequence[n]


# Memoize decorator and top-down approach
class Memoize:
    def __init__(self, func):
        self.func = func
        self.memo = {0: [0], 1: [1]}

    def __call__(self, n):
        if n not in self.memo:
            self.memo[n] = self.func(n)
        return self.memo[n]


@Memoize
def optimal_seq(n):
    seq = optimal_seq(n-1)[:]
    seq.append(n)
    opt_len = len(seq)
    if n % 3 == 0:
        other = optimal_seq(n//3)[:]
        if len(other) < opt_len - 1:
            seq = other
            seq.append(n)
    if n % 2 == 0:
        other = optimal_seq(n//2)[:]
        if len(other) < opt_len - 1:
            seq = other
            seq.append(n)
    return seq


# memoize with lru_cache()
@functools.lru_cache(maxsize=5000)
def opt_seq(n):
    if n == 0:
        return [0]
    if n == 1:
        return [1]
    seq = opt_seq(n-1)[:]
    seq.append(n)
    opt_len = len(seq)
    if n % 3 == 0:
        other = opt_seq(n//3)[:]
        if len(other) < opt_len - 1:
            seq = other
            seq.append(n)
    if n % 2 == 0:
        other = opt_seq(n//2)[:]
        if len(other) < opt_len - 1:
            seq = other
            seq.append(n)
    return seq


if __name__ == '__main__':
    # input_ = sys.stdin.read()
    # n = int(input_)
    # sequence = list(optimal_sequence(n))
    # print(len(sequence) - 1)
    # for x in sequence:
    #     print(x, end=' ')
    sys.setrecursionlimit(100000)
    with open('input.txt') as f:
        input_ = f.read()
        n = int(input_)
        t0 = time.time()
        sequence = list(optimal_sequence(n))
        t0 = time.time() - t0
        print(len(sequence) - 1)
        for x in sequence:
            print(x, end=' ')
        print('Running time 1: {0:5f}s'.format(t0))

        t1 = time.time()
        sequence = list(optimal_seq(n))
        t1 = time.time() - t1
        print(len(sequence) - 1)
        for x in sequence:
            print(x, end=' ')
        print('Running time 2: {0:5f}s'.format(t1))
