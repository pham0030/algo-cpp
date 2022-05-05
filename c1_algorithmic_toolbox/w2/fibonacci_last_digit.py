# Uses python3
import sys
import random


# Naive fibonacci last digit
def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % 10


def get_fibonacci_last_digit_less_mem(n):
    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current, (previous + current) % 10

    return current

if __name__ == '__main__':
    # input = sys.stdin.read()
    # n = int(input)
    # print(get_fibonacci_last_digit_naive(n))

    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit_less_mem(n))

    # Stress test
    # while(True):
    #     n = random.randint(0, 10000)
    #     less_mem = get_fibonacci_last_digit_less_mem(n)
    #     print(less_mem)
    #     naive = get_fibonacci_last_digit_naive(n)
    #     print(naive)
    #     if (naive != less_mem):
    #         print('Wrong answer: naive: {} less_mem: {}\n'.
    #               format(naive, less_mem))
    #         break
    #     else:
    #         print('Ok!\n')

    # Overflow/Memory Test
    # n = int(1e7)
    # print(get_fibonacci_last_digit_less_mem(n))
