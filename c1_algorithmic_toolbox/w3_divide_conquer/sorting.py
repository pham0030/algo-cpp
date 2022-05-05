# Uses python3
import sys
import random


def partition2(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    # use partition2
    m = partition2(a, l, r)
    randomized_quick_sort(a, l, m - 1)
    randomized_quick_sort(a, m + 1, r)


# implementation of partiotion3 with while loop
def partition3while(a, l, r):
    x = a[l]
    m1 = l
    m2 = r
    i = m1
    while i <= m2:
        if a[i] < x:
            a[m1], a[i] = a[i], a[m1]
            m1 += 1
        if a[i] > x:
            a[m2], a[i] = a[i], a[m2]
            m2 -= 1
            i -= 1
        i += 1
    return m1, m2


# implementation of partiotion3 with for loop
def partition3(a, l, r):
    x = a[l]
    m1 = l
    m2 = l
    i = m1
    for i in range(l + 1, r + 1):
        if a[i] < x:
            a[i], a[m1] = a[m1], a[i]
            a[i], a[m2+1] = a[m2+1], a[i]
            m1 += 1
            m2 += 1
        elif a[i] == x:
            a[i], a[m2+1] = a[m2+1], a[i]
            m2 += 1
    return m1, m2


def randomized_quick3_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    # use partition3
    m1, m2 = partition3(a, l, r)
    randomized_quick3_sort(a, l, m1 - 1)
    randomized_quick3_sort(a, m2 + 1, r)


def merge(left, right, a):
    i, j, k = 0, 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            a[k], i, k = left[i], i + 1, k + 1
        else:
            a[k], j, k = right[j], j + 1, k + 1
    while i < len(left):
        a[k], i, k = left[i], i + 1, k + 1
    while j < len(right):
        a[k], j, k = right[j], j + 1, k + 1


def merge_sort(a):
    if len(a) < 2:
        return
    mid = len(a)//2
    left = a[:mid]
    right = a[mid:]
    merge_sort(left)
    merge_sort(right)
    return merge(left, right, a)


if __name__ == '__main__':
    # input = sys.stdin.read()
    # n, *a = list(map(int, input.split()))
    # randomized_quick3_sort(a, 0, n - 1)
    # for x in a:
    #     print(x, end=' ')

    # Debug Simple
    # with open('input.txt') as f:
    #     input = f.read()
    #     n, *a = list(map(int, input.split()))
    #     randomized_quick3_sort(a, 0, n - 1)
    #     for x in a:
    #         print(x, end=' ')
    #     print()

    # Stress test
    i = 1
    while(True):
        print('Test: {}'.format(i))
        a = [random.randint(1, int(1e2))
             for _ in range(1, random.randint(1, int(1e2)))]
        b = a[:]
        b.sort()
        # randomized_quick3_sort(a, 0, r=len(a)-1)
        merge_sort(a)
        if a == b:
            print('Ok!')
        else:
            print('Wrong')
            print(a)
            print(b)
            break
        i += 1
