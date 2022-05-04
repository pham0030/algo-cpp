# Uses python3


def evalt(a, op, b):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False


def get_maximum_value(dataset):

    d = [int(x) for x in dataset[0::2]]
    op = dataset[1::2]
    n = len(d)
    m = [[None] * n for _ in range(n)]
    M = [[None] * n for _ in range(n)]
    for i in range(n):
        m[i][i] = d[i]
        M[i][i] = d[i]

    for s in range(1, n):
        for i in range(n-s):
            j = i + s
            m[i][j] = float('inf')
            M[i][j] = float('-inf')
            for k in range(i, j):
                a = evalt(M[i][k], op[k], M[k+1][j])
                b = evalt(M[i][k], op[k], m[k+1][j])
                c = evalt(m[i][k], op[k], M[k+1][j])
                d = evalt(m[i][k], op[k], m[k+1][j])
                m[i][j] = min(m[i][j], a, b, c, d)
                M[i][j] = max(M[i][j], a, b, c, d)

    # print('m:', type(m))
    # for i in range(n):
    #     for j in range(n):
    #         print(m[i][j], end=' ')
    #     print()
    # print('M:', type(m))
    # for i in range(n):
    #     for j in range(n):
    #         print(M[i][j], end=' ')
    #     print()
    return M[0][-1]


if __name__ == "__main__":
    print(get_maximum_value(input()))

    # with open('input.txt') as f:
    #     print(get_maximum_value(f.read()))
