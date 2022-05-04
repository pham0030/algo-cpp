# python3

EPS = 1e-6


class Equation:
    def __init__(self, a, b):
        self.a = a
        self.b = b


class Position:
    def __init__(self, row, column):
        self.row = row
        self.column = column


def read_equation():
    size = int(input())
    a = []
    b = []
    for row in range(size):
        line = list(map(float, input().split()))
        a.append(line[:size])
        b.append(line[size])
    return Equation(a, b)


def select_pivot_element(a, step):
    # Choose pivot at the step-th column and step-th row
    # If the pivot is zero then move the pivot to the next
    # step-th + 1 row
    for i in range(step, len(a)):
        if abs(a[i][step]) > EPS:
            return Position(i, step)
    raise ValueError


def swap_lines(a, b, used_rows, pivot_element):
    a[pivot_element.row], a[pivot_element.column] = \
        a[pivot_element.column], a[pivot_element.row]
    b[pivot_element.row], b[pivot_element.column] = \
        b[pivot_element.column], b[pivot_element.row]
    used_rows[pivot_element.row], used_rows[pivot_element.column] = \
        used_rows[pivot_element.column], used_rows[pivot_element.row]
    pivot_element.row = pivot_element.column


def process_pivot_element(a, b, pivot_element):
    for i in range(pivot_element.column+1, len(b)):  # iterate over row
        alpha = \
          a[i][pivot_element.column]/a[pivot_element.row][pivot_element.column]
        b[i] -= b[pivot_element.row]*alpha
        for j in range(pivot_element.column, len(a)):  # iterate over column
            a[i][j] -= a[pivot_element.row][j] * alpha


def make_pivot_element_used(pivot_element, used_rows, used_columns):
    used_rows[pivot_element.row] = True
    used_columns[pivot_element.column] = True


def solve_equation(equation):
    a = equation.a
    b = equation.b
    size = len(a)

    used_columns = [False] * size
    used_rows = [False] * size
    for step in range(size):
        pivot_element = select_pivot_element(a, step)
        swap_lines(a, b, used_rows, pivot_element)
        process_pivot_element(a, b, pivot_element)
        make_pivot_element_used(pivot_element, used_rows, used_columns)

    for i in reversed(range(len(a))):
        first_coef = a[i][i]
        if first_coef == 0:
            raise ValueError
        for j in range(i+1, len(a)):
            b[i] -= b[j] * a[i][j]
        b[i] /= first_coef
    return b


def print_result(column):
    size = len(column)
    for row in range(size):
        print("%.3lf" % column[row], end=' ')

if __name__ == "__main__":
    equation = read_equation()
    solution = solve_equation(equation)
    print_result(solution)
