# Uses python3
import sys
import random


def is_greater_or_equal(a, b):
    ab = a + b
    ba = b + a
    if int(ab) >= int(ba):
        greater_or_equal = True
    else:
        greater_or_equal = False
    return greater_or_equal


def largest_number(a):
    ans = ""
    while len(a) >= 1:
        max_digit = '0'
        for digit in a:
            if is_greater_or_equal(digit, max_digit):
                max_digit = digit
        ans += max_digit
        a.pop(a.index(max_digit))
    return ans


if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))

    # Debug
    # with open('input.txt') as f:
    #     input = f.read()
    # data = input.split()
    # a = data[1:]
    # print(largest_number(a))
