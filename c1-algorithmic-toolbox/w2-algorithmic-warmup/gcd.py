# Uses python3
import sys
import random
import time


# Naive gcd
def gcd_naive(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd


# Euclidean
def gcd_euclidean(a, b):
    if a >= b:
        if b == 0:
            return a
        else:
            a_prime = a % b
            return gcd_euclidean(b, a_prime)
    else:
        if a == 0:
            return b
        else:
            b_prime = b % a
            return gcd_euclidean(a, b_prime)


if __name__ == "__main__":
    # input = sys.stdin.read()
    # a, b = map(int, input.split())
    # print(gcd_naive(a, b))

    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd_euclidean(a, b))

    # Stress test
    # random.seed(1)
    # i = 0
    # while (True):
    #     print('Test: {}'.format(i))
    #     a = int(2000000*random.random() + 1)
    #     b = int(20000000*random.random() + 1)
    #     print("gcd_euclidean({}, {})".format(a, b), end=' = ')
    #     t0 = time.time()
    #     euclidean = gcd_euclidean(a, b)
    #     t = time.time() - t0
    #     print(euclidean)
    #     print('computing time : {} s'.format(t))

    #     print("gcd_naive({}, {})".format(a, b), end=' = ')
    #     t0 = time.time()
    #     naive = gcd_naive(a, b)
    #     t = time.time() - t0
    #     print(naive)
    #     print('computing time : {} s'.format(t))
    #     if(naive != euclidean):
    #         print("Miss match \n".
    #               format(naive, euclidean))
    #         break
    #     else:
    #         print("Ok!\n")
    #     i += 1
