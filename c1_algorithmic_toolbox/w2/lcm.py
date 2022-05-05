# Uses python3
import sys
import random
import time


def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b


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


def lcm_fast(a, b):
    return a * b // gcd_euclidean(a, b)


if __name__ == '__main__':
    # input = sys.stdin.read()
    # a, b = map(int, input.split())
    # print(lcm_naive(a, b))

    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_fast(a, b))

    # Stress test
    # random.seed(1)
    # i = 0
    # while (True):
    #     print('Test: {}'.format(i))
    #     a = int(2000*random.random() + 1)
    #     b = int(2000*random.random() + 1)
    #     print("lcm_fast({}, {})".format(a, b), end=' = ')
    #     t0 = time.time()
    #     fast = lcm_fast(a, b)
    #     t = time.time() - t0
    #     print(fast)
    #     print('computing time : {} s'.format(t))

    #     print("lcm_naive({}, {})".format(a, b), end=' = ')
    #     t0 = time.time()
    #     naive = lcm_naive(a, b)
    #     t = time.time() - t0
    #     print(naive)
    #     print('computing time : {} s'.format(t))
    #     if(naive != fast):
    #         print("Miss match \n".
    #               format(naive, fast))
    #         break
    #     else:
    #         print("Ok!\n")
    #     i += 1
