# Uses python3
import sys
import random


def fibonacci_partial_sum_naive(from_, to):
    sum = 0

    current = 0
    next = 1

    for i in range(to + 1):
        if i >= from_:
            sum += current

        current, next = next, current + next

    return sum % 10


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


def fibonacci_partial_sum_fast(m, n):
    # m : from_
    # n : to
    # partial fibonacci sum from (m, n) = F(n+2) - F(m+1)

    # Last digit of F(n+2)
    last1 = get_fibonacci_huge_fast(n+2, 10)
    # Last digit of F(m+1)
    last2 = get_fibonacci_huge_fast(m+1, 10)
    return (last1 + 10 - last2) % 10


if __name__ == '__main__':
    # input = sys.stdin.read()
    # from_, to = map(int, input.split())
    # print(fibonacci_partial_sum_naive(from_, to))

    # Stress test
    # while(True):
    #     from_ = random.randint(0, 10000)
    #     to = from_ + random.randint(0, 10000)
    #     fast = fibonacci_partial_sum_fast(from_, to)
    #     print(fast)
    #     naive = fibonacci_partial_sum_naive(from_, to)
    #     print(naive)
    #     if (naive != fast):
    #         print('Wrong answer: naive: {} fast: {}\n'.format(naive, fast))
    #         break
    #     else:
    #         print('Ok!\n')

    # Overflow test
    # from_ = int(1e18)
    # to = int(1e17)
    # print(fibonacci_partial_sum_fast(from_, to))

    input = sys.stdin.read()
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum_fast(from_, to))
