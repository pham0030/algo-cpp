# python3
import sys


def bwt_transform(input_text):
    list_s = [input_text]
    for _ in range(len(input_text) - 1):
        list_s.append(list_s[-1][-1] + list_s[-1][:-1])
    list_s.sort()
    res = "".join(s[-1] for s in list_s)
    return res

if __name__ == '__main__':

    input_text = sys.stdin.readline().strip()
    print(bwt_transform(input_text))
