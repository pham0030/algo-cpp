# Uses python3
import sys
import random


def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current = 1
    sum = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current

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


def fibonacci_sum_fast(n):
    # Sum of first F(n) = F(n + 2) - 1
    res = get_fibonacci_huge_fast(n + 2, 10)
    if res == 0:
        return 9
    else:
        return res - 1


if __name__ == '__main__':
    # input = sys.stdin.read()
    # n = int(input)
    # print(fibonacci_sum_naive(n))

    # Stress test
    # while(True):
    #     n = random.randint(0, 10000)
    #     fast = fibonacci_sum_fast(n)
    #     print(fast)
    #     naive = fibonacci_sum_naive(n)
    #     print(naive)
    #     if (naive != fast):
    #         print('Wrong answer: naive: {} fast: {}\n'.format(naive, fast))
    #         break
    #     else:
    #         print('Ok!\n')

    # Overflow/memory test
    # n = int(1e15)
    # print(fibonacci_sum_fast(n))

    input = sys.stdin.read()
    n = int(input)
    print(fibonacci_sum_fast(n))
