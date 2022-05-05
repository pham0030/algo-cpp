# python3
from sys import stdin

EPS = 1e-6


def solve_diet_problem(n, m, A, b, c):
    flag = None
    ineq_idx = [i for i in range(n+m+1)]
    subset = [None]*m
    all_subsets = []
    all_subsets = get_all_subsets(ineq_idx, m, 0, subset, all_subsets)
    for subset in all_subsets:
        # chose the subset from the inequalities
        new_A = [[0. for _ in range(m)] for _ in range(m)]
        new_b = [0. for _ in range(m)]
        cut_row(A, b, new_A, new_b, subset)
        solution = []
        try:
            solution = solve_linear_equations(new_A, new_b)
        except ValueError as err:
            continue

        remaining_indices = [i for i in range(n+m+1) if i not in subset]
        remaining_inequalities = [[0. for _ in range(m)]
                                  for _ in range(len(remaining_indices))]
        remaining_b = [0. for _ in range(len(remaining_indices))]
        cut_row(A, b, remaining_inequalities, remaining_b, remaining_indices)
        if check_solution(solution, remaining_inequalities, remaining_b):
            optimizing_expression_value = 0.
            for j in range(len(solution)):
                optimizing_expression_value += solution[j]*c[j]
            if flag is None or optimizing_expression_value > flag:
                flag = optimizing_expression_value
                main_solution = solution[:]

    if flag is None:
        return -1, None
    if flag > 999999999:
        return 1, None
    return 0, main_solution


def get_all_subsets(arr, len_subset, start_pos, subset, all_subsets):
    if len_subset == 0:
        all_subsets.append(subset[:])
        return all_subsets
    for i in range(start_pos, len(arr)-len_subset+1):
        subset[len(subset) - len_subset] = arr[i]
        get_all_subsets(arr, len_subset-1, i+1, subset, all_subsets)
    return all_subsets


def cut_row(A, b, new_A, new_b, subset):
    n = len(A)
    m = len(A[0])
    for i in range(len(subset)):
        # first n inequalities, indices: 0 -> n-1
        if subset[i] < n:
            new_A[i] = A[subset[i]][:]
            new_b[i] = b[subset[i]]
        # additional last inequality to deal with Infinity case
        # index: n+m
        elif subset[i] == n + m:
            new_A[i] = [1] * m
            new_b[i] = 10e9
        # inequalities to account for non negative conditions of
        # amount of the ingredients, indices: n -> n+m-1
        else:
            new_A[i][subset[i] - n] = -1
    return new_A, new_b


# Function to check if the found vertex satisfy all the conditions
def check_solution(solution, remaining_inequalities, rem_b):
    for i in range(len(remaining_inequalities)):
        inequality = remaining_inequalities[i]
        sum_ = 0.
        for j in range(len(inequality)):
            sum_ += solution[j] * inequality[j]
        if sum_ > rem_b[i]:
            return False
    return True


# Gaussian Elimination to solve linear equations
class Equation:
    def __init__(self, a, b):
        self.a = a
        self.b = b


class Position:
    def __init__(self, row, column):
        self.row = row
        self.column = column


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


def make_pivot_element_used(pivot_element, used_rows, used_columns):
    used_rows[pivot_element.row] = True
    used_columns[pivot_element.column] = True


def process_pivot_element(a, b, pivot_element):
    for i in range(pivot_element.column+1, len(b)):  # iterate over row
        alpha = \
          a[i][pivot_element.column]/a[pivot_element.row][pivot_element.column]
        b[i] -= b[pivot_element.row]*alpha
        for j in range(pivot_element.column, len(a)):  # iterate over column
            a[i][j] -= a[pivot_element.row][j] * alpha


def solve_linear_equations(a, b):
    # a[m*m]
    # b[1*m]
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


if __name__ == "__main__":
    # n: number of restrictions (no of linear inequalities)
    # m: number of available dishes and drinks (no of variables)
    n, m = list(map(int, stdin.readline().split()))

    # matrix A[n*m]: coefficient of n linear inequalities and
    # m variables
    A = []
    for i in range(n):
        A += [list(map(int, stdin.readline().split()))]
    # b[1*n]: right hand side of the linear inequalities
    b = list(map(int, stdin.readline().split()))

    # c[1*m]: coefficient of expression to maximize
    c = list(map(int, stdin.readline().split()))

    anst, ansx = solve_diet_problem(n, m, A, b, c)
    if anst == -1:
        print("No solution")
    if anst == 0:
        print("Bounded solution")
        print(' '.join(list(map(lambda x: '%.18f' % x, ansx))))
    if anst == 1:
        print("Infinity")
