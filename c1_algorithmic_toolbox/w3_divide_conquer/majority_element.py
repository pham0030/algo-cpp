# Uses python3
import sys
import random


def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    mid = (left + right)//2
    left_majority = get_majority_element(a, left, mid)
    right_majority = get_majority_element(a, mid, right)

    # check if left_majority is majority in the right
    left_count = 0
    for i in range(left, right):
        if left_majority == a[i]:
            left_count += 1
    if left_count > (right-left)//2:
        return left_majority

    # check if right_majority is majority in the left
    right_count = 0
    for j in range(left, right):
        if right_majority == a[j]:
            right_count += 1
    if right_count > (right-left)//2:
        return right_majority
    return -1


def get_majority_element_naive(a, left, right):
    assert(right == len(a))
    for i in range(len(a)):
        current_el = a[i]
        count = 0
        for j in range(len(a)):
            if a[j] == current_el:
                count += 1
        if count > (right-left)//2:
            return a[i]
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)

    # Simple debug
    # with open('input.txt') as f:
    #     input = f.read()
    #     n, *a = list(map(int, input.split()))
    #     print(get_majority_element(a, 0, n))

    # Stress test:
    # i = 1
    # while(i < 1000):
    #     print('Test: {}'.format(i))
    #     m = random.randint(0, int(1e9))
    #     a = [m] * random.randint(1, 1e5)
    #     a_e = [random.randint(0, int(1e9)) for _ in
    #            range(len(a)//2 - random.randint(0, len(a)//2))]
    #     a.extend(a_e)
    #     random.shuffle(a)

    #     ans = get_majority_element_naive(a, 0, len(a))
    #     if ans != m:
    #         print('Wrong: m:{} ans:{}'.format(m, ans))
    #         print('a:', a)
    #         break
    #     else:
    #         print('Ok')
    #     i += 1
