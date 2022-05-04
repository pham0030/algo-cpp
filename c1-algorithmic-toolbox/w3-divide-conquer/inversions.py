# Uses python3
import sys
import random
import time


# def get_number_of_inversions(a, b, left, right):
#     number_of_inversions = 0
#     if right - left <= 1:
#         return number_of_inversions
#     ave = (left + right) // 2
#     number_of_inversions += get_number_of_inversions(a, b, left, ave)
#     number_of_inversions += get_number_of_inversions(a, b, ave, right)
#     # write your code here
#     return number_of_inversions


def merge(left, right, a):
    i, j, k = 0, 0, 0
    mid = len(left)
    number_of_inversions = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            a[k], i, k = left[i], i + 1, k + 1
        else:
            a[k], j, k = right[j], j + 1, k + 1
            number_of_inversions += mid - i
    while i < len(left):
        a[k], i, k = left[i], i + 1, k + 1
    while j < len(right):
        a[k], j, k = right[j], j + 1, k + 1
    return number_of_inversions


def get_number_of_inversions(a):
    number_of_inversions = 0
    if len(a) < 2:
        return number_of_inversions
    mid = len(a) // 2
    left = a[:mid]
    right = a[mid:]
    number_of_inversions += get_number_of_inversions(left)
    number_of_inversions += get_number_of_inversions(right)
    number_of_inversions += merge(left, right, a)
    return number_of_inversions


def get_number_of_inversions_naive(a):
    number_of_inversions = 0
    for i in range(len(a)-1):
        for j in range(i+1, len(a)):
            if a[i] > a[j]:
                number_of_inversions += 1
    return number_of_inversions

if __name__ == '__main__':
    # input = sys.stdin.read()
    # n, *a = list(map(int, input.split()))
    # b = n * [0]
    # print(get_number_of_inversions(a, b, 0, len(a)))

    # Final
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    print(get_number_of_inversions(a))

    # Debug Simple
    # input = sys.stdin.read()
    # n, *a = list(map(int, input.split()))
    # assert(n == len(a))
    # b = a[:]
    # print(get_number_of_inversions(a))
    # print(get_number_of_inversions_naive(b))

    # Stress test:
    # i = 1
    # while(True):
    #     print('Test:{}'.format(i))
    #     n = random.randint(1, int(1e4))
    #     a = [random.randint(1, int(1e3)) for _ in range(n)]
    #     ans1 = get_number_of_inversions_naive(a)
    #     ans2 = get_number_of_inversions(a)
    #     if ans1 != ans2:
    #         print('Wrong: ans1:{}, ans2:{}'.format(ans1, ans2))
    #         break
    #     else:
    #         print('Ok')
    #     i += 1

    # Speed test:
    # n = int(1e5)
    # a = [random.randint(1, int(1e3)) for _ in range(n)]
    # t0 = time.time()
    # ans1 = get_number_of_inversions_naive(a)
    # t = time.time() - t0
    # print('Naive:{}, time:{}'.format(ans1, t))
    # t0 = time.time()
    # ans2 = get_number_of_inversions(a)
    # t = time.time() - t0
    # print('Fast:{}, time:{}'.format(ans2, t))
