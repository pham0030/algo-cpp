# Uses python3
import random


# Naive recursive fibonacci
def calc_fib(n):
    if (n <= 1):
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)


# Array fibonacci
def calc_fib_fast(n):
    if n <= 1:
        return n
    else:
        fib_array = [0] * (n + 1)
        fib_array[0] = 0
        fib_array[1] = 1
        for i in range(2, n + 1):
            fib_array[i] = fib_array[i - 1] + fib_array[i - 2]
        return fib_array[-1]

if __name__ == '__main__':
    # n = int(input())
    # print(calc_fib(n))
    # print(calc_fib_fast(n))

    n = int(input())
    print(calc_fib_fast(n))

    # Stress test
    # while(True):
    #     n = random.randint(0, 35)
    #     fast = calc_fib_fast(n)
    #     print(fast)
    #     naive = calc_fib(n)
    #     print(naive)
    #     if (naive != fast):
    #         print('Wrong answer: naive: {} fast: {}\n'.format(naive, fast))
    #         break
    #     else:
    #         print('Ok!\n')
