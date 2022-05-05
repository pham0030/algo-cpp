# Uses python3
import sys
import random


def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m


def get_pisano_period_naive(m):
    a = 0
    b = 1
    if m < 2:
        return 1
    else:
        for i in range(m*m):
            c = a + b
            b_p = b % m
            c_p = c % m
            a = b
            b = c
            if (b_p == 0 and c_p == 1):
                return i + 1


def get_pisano_period(m):
    a = 0
    b = 1
    if m < 2:
        return 1
    else:
        for i in range(m*m):
            c = (a + b) % m
            a = b
            b = c
            if (a == 0 and b == 1):
                return i + 1


def get_fibonacci_huge_fast(n, m):
    remainder = n % get_pisano_period(m)
    if n <= 1:
        return n

    a = 0
    b = 1
    res = remainder
    for i in range(remainder - 1):
        res = (a + b) % m
        a = b
        b = res
    return res


if __name__ == '__main__':
    # input = sys.stdin.read()
    # n, m = map(int, input.split())
    # print(get_fibonacci_huge_naive(n, m))

    # Stress test get_pisano_period(m)
    # while(True):
    #     m = random.randint(0, 100000)
    #     print('Stress testing get_pisano_period mod {}'.format(m), end=':')
    #     period_naive = get_pisano_period_naive(m)
    #     period = get_pisano_period(m)
    #     if period_naive != period:
    #         print('Miss match pisano period: naive: {} fast: {}'
    #               .format(period_naive, period))
    #         break
    #     else:
    #         print('Ok!')

    # Stress test get_fibonnaci_huge_fast(n, m)
    # while(True):
    #     # n = 10
    #     n = random.randint(0, 100000)
    #     m = random.randint(0, 100000)
    #     print('Stress testing get_fibonacci_huge_fast n:{} mod {}'.
    #           format(n, m))
    #     naive = get_fibonacci_huge_naive(n, m)
    #     fast = get_fibonacci_huge_fast(n, m)
    #     if naive != fast:
    #         print('Miss match : naive: {} fast: {}'.format(naive, fast))
    #         break
    #     else:
    #         print('Ok!')

    # Overflow stress test
    # while(True):
    #     try:
    #         n = random.randint(0, int(1e18))
    #         m = random.randint(0, 100000)
    #         res = get_fibonacci_huge_fast(n, m)
    #         print(res)
    #     except Exception as err:
    #         print(err)
    #         break

    input = sys.stdin.read()
    n, m = map(int, input.split())
    print(get_fibonacci_huge_fast(n, m))
