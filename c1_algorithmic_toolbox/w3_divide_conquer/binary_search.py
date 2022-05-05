# Uses python3
import sys
import random


def binary_search(a, x):
    def recurse(a, low, high, x):
        if high < low:
            return -1
        mid = (low + high)//2
        if x == a[mid]:
            return mid
        elif x < a[mid]:
            return recurse(a, low, mid-1, x)
        else:
            return recurse(a, mid+1, high, x)
    return recurse(a, 0, len(a)-1, x)


def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1


def linear_recursive_search(a, x):
    def recurse(a, low, high, x):
        if high < low:
            return -1
        if a[low] == x:
            return low
        return recurse(a, low+1, high, x)
    return recurse(a, 0, len(a)-1, x)


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1: n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print(binary_search(a, x), end=' ')

    # with open('input.txt') as f:
    #     input = f.read()
    #     data = list(map(int, input.split()))
    #     n = data[0]
    #     m = data[n + 1]
    #     a = data[1: n + 1]
    #     for x in data[n + 2:]:
    #         print(linear_recursive_search(a, x), end=' ')
    #     print()

    # Stress test
    # i = 1
    # while(True):
    #     print('Test: {}'.format(i))
    #     n = random.randint(0, int(1e5))
    #     a = sorted(random.sample(range(int(1e9)), n))
    #     x = random.randint(0, int(1e9))
    #     s1 = linear_search(a, x)
    #     s2 = binary_search(a, x)
    #     if s1 != s2:
    #         print(x, a)
    #         print('Not match: s1:{} s2:{}'.format(s1, s2))
    #         break
    #     else:
    #         print('Ok')
    #     i += 1
