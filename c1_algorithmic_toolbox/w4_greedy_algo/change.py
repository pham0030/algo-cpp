# Uses python3
import sys


def get_change(m):
    if not isinstance(m, int):
        raise ValueError('input is not integer')
    else:
        n_ten = m//10
        n_five = (m - n_ten*10)//5
        n_one = m - n_ten*10 - n_five*5
        n = n_ten + n_five + n_one
        return n

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
