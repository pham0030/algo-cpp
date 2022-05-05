# python3
import sys


def inverse_BWT(bwt):
    # write your code here
    last_column = [(val, idx) for idx, val in enumerate(bwt)]
    first_column = sorted(last_column)
    last_to_first = {last: first for first, last in
                     zip(first_column, last_column)}
    counter_position = first_column[0]
    res = ""
    for i in range(len(bwt)):
        res += last_to_first[counter_position][0]
        counter_position = last_to_first[counter_position]
    return res


if __name__ == '__main__':
    bwt = sys.stdin.readline().strip()
    print(inverse_BWT(bwt))
