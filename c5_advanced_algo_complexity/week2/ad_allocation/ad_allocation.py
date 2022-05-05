# python3
from sys import stdin
import numpy as np
warning_off = np.seterr(all='ignore')
eps = 1e-10


class Simplex2P:

    def __init__(self):
        self.num_constraints = None
        self.num_vars = None
        self.A = None
        self.RHS = None
        self.z = None  # objective expression to be maximized

        self.table = None
        self.artificial_vars = {}
        self.special_artificial_vars = {}
        self.art_vars_kept = set()
        self.flag = None  # Infinity, Bounded solution or No solution
        self.basis = {}
        self.solution = None

    def read_data_console(self):
        self.num_constraints, self.num_vars = list(map(int, stdin.readline().split()))
        self.A = []
        for i in range(self.num_constraints):
            self.A += [list(map(int, stdin.readline().split()))]
        self.RHS = list(map(int, stdin.readline().split()))
        self.z = list(map(int, stdin.readline().split()))

    def read_data_file(self, file_path):
        with open(file_path) as f:
            self.num_constraints, self.num_vars = list(map(int, f.readline().split()))
            self.A = []
            for i in range(self.num_constraints):
                self.A += [list(map(float, f.readline().split()))]
            self.RHS = list(map(float, f.readline().split()))
            self.z = list(map(float, f.readline().split()))

    def add_artificial(self):
        # Add a non-negative artificial variable to any equation that
        # does not have an isolated variable readily apparent
        for col in range(self.num_vars, self.num_vars+self.num_constraints):
            if np.sum(self.table[:, col]) != 1:
                art_var = np.zeros((self.num_constraints, 1))
                art_var[col - self.num_vars] = 1.0
                self.basis[col - self.num_vars] = len(self.table[0])-1
                self.artificial_vars[col - self.num_vars] = len(self.table[0]) - 1
                self.table = np.hstack((self.table, art_var))
                self.table[:, (-2, -1)] = self.table[:, (-1, -2)]  # swap to correct place

    def place_canonical_constraints(self):
        self.table = np.array(self.A)

        # only slack variables are included as the inequalities are <= only
        self.table = np.hstack((self.table, np.eye(self.num_constraints, dtype=float)))
        for row in range(self.num_constraints):
            self.basis[row] = row + self.num_vars

        rhs = np.array(self.RHS)
        self.table = np.hstack((self.table, rhs[:, np.newaxis]))

        # multiply equations with negative right hand side
        for row, x in enumerate(self.table[:, -1]):  # last column of table
            if x < 0:
                self.table[row] *= -1.0
        # t1 = time.time()
        self.add_artificial()
        # print(time.time() - t1)

    def pivot_about(self, pivot_row, pivot_col):
        self.table[pivot_row, :] /= self.table[pivot_row, pivot_col]

        # for idx, row in enumerate(self.table):
        #     if idx != pivot_row:
        #         multiple = row[pivot_col] / self.table[pivot_row, pivot_col]
        #         row -= multiple * self.table[pivot_row, :]
        # self.basis[pivot_row] = pivot_col

        col = np.copy(self.table[:, pivot_col])
        col[pivot_row] = 0
        mask = col[:, np.newaxis] * self.table[pivot_row]
        self.table -= mask
        self.basis[pivot_row] = pivot_col

    def simplex_phase1(self):
        # Loop until optimal point is reached or unbounded solution is
        # detected
        while not np.all(self.table[-1][:-1] >= 0):
            pivot_col = np.argmin(self.table[-1][:-1])
            # Check for Infinity/Unbounded criterion
            if np.all(self.table[:, pivot_col][:-1] <= 0):
                return 'Infinity'
            theta = self.table[:-1, -1] / self.table[:-1, pivot_col]
            theta[self.table[:-1, -1] <= 0] = float('inf')
            theta[self.table[:-1, pivot_col] <= 0] = float('inf')
            pivot_row = np.argmin(theta)
            self.pivot_about(pivot_row, pivot_col)

        # The problem is infeasible if artificial var is still basis
        # solution of the auxiliary problem with value not zero
        # NEED TO HANDLE SPECIAL CASE where artificial var
        # is still in the basis but value is equal to zero
        for row, col in self.artificial_vars.items():
            if col == self.basis[row]:
                if abs(self.table[row, -1]) <= eps:
                    self.special_artificial_vars[row] = col
                else:  # special artificial vars
                    return 'No solution'

        if self.special_artificial_vars:
            return 'Special'
        else:
            return 'Feasible'

    def simplex_phase2(self):
        # Loop until optimal point is reached or unbounded solution is
        # detected
        while not np.all(self.table[-1][:-1] >= 0):
            pivot_col = np.argmin(self.table[-1][:-1])
            # Check for Infinity/Unbounded criterion
            if np.all(self.table[:, pivot_col][:-1] <= 0):
                return 'Infinity'
            # Pivoting
            theta = self.table[:-1, -1] / self.table[:-1, pivot_col]
            theta[self.table[:-1, -1] < 0] = float('inf')
            theta[self.table[:-1, pivot_col] < 0] = float('inf')
            theta[np.logical_and(
                  self.table[:-1, -1] == 0,
                  self.table[:-1, pivot_col] == 0)] = float('inf')
            if not np.any(np.isfinite(theta)):
                return 'Infinity'
            pivot_row = np.argmin(theta)
            self.pivot_about(pivot_row, pivot_col)

        self.solution = [0.]*self.num_vars
        for row, col in self.basis.items():
            if col < self.num_vars:
                self.solution[col] = self.table[:, -1][row]

        return 'Bounded solution'

    def two_phase(self):
        if self.artificial_vars:  # phase 1 condition
            # add auxiliary objective w-equation
            w = np.zeros((1, len(self.table[0])))
            for row in self.artificial_vars:
                w -= self.table[row, :]
            for col in self.artificial_vars.values():
                w[0, col] = 0
            self.table = np.vstack((self.table, w))
            # phase 1 start
            self.flag = self.simplex_phase1()
            if self.flag == 'Feasible' or self.flag == 'Infinity':
                # fixing for phase 2
                # remove artificial variables by masking it with 0
                # self.table = np.delete(self.table, tuple(self.artificial_vars.values()), 1)
                self.table[:, tuple(self.artificial_vars.values())] = 0
                # remove auxiliary objectives
                self.table = np.delete(self.table, -1, 0)
                # add original objective z-equation
                z = -1 * np.array(self.z)
                z = np.hstack((z, np.zeros(self.num_constraints + len(self.artificial_vars) + 1)))
                self.table = np.vstack((self.table, z))
                # fix the corrupted canonical vectors (basis)
                for row, col in self.basis.items():
                    if self.table[-1, col] != 0:
                        self.table[-1] -= self.table[-1, col] / self.table[row, col] \
                                          * self.table[row]
                # run the simplex method phase 2
                self.flag = self.simplex_phase2()
            elif self.flag == 'Special':
                for art_row, art_col in self.special_artificial_vars.items():
                    # check if we can remove special artificial vars
                    non_zero = np.nonzero(self.table[art_row, :(self.num_vars+self.num_constraints)])
                    non_zero = non_zero[0]
                    if non_zero.size > 0:  # pivoting to remove this special vars from table
                        pivot_col = non_zero[0]
                        self.pivot_about(art_row, pivot_col)
                    else:
                        self.art_vars_kept.add(art_col)
                # remove artificial variables by masking it with 0, keep art_vars_kept
                # by not masking them
                art_cols = set(self.artificial_vars.values())
                vars_to_be_masked = art_cols.difference(self.art_vars_kept)
                self.table[:, tuple(vars_to_be_masked)] = 0
                # remove auxiliary objectives
                self.table = np.delete(self.table, -1, 0)
                # add original objective z-equation
                z = -1 * np.array(self.z)
                z = np.hstack((z, np.zeros(self.num_constraints + len(self.artificial_vars) + 1)))
                self.table = np.vstack((self.table, z))
                # fix the corrupted canonical vectors (basis)
                for row, col in self.basis.items():
                    if self.table[-1, col] != 0:
                        self.table[-1] -= self.table[-1, col] / self.table[row, col] \
                                          * self.table[row]
                # run the simplex method phase 2
                # t2 = time.time()
                self.flag = self.simplex_phase2()
                # print(time.time() - t2)
            else:
                pass
        else:  # phase 2 preparation
            # add original  objective z-equation
            z = -1 * np.array(self.z)
            z = np.hstack((z, np.zeros(self.num_constraints + 1)))
            self.table = np.vstack((self.table, z))
            # run the simplex method phase 2
            # t2 = time.time()
            self.flag = self.simplex_phase2()
            # print(time.time() - t2)


if __name__ == '__main__':

    # import os
    # import time
    # t0 = time.time()
    # cwd = os.getcwd()
    # test_case = 'tests/44'
    # file_path = os.path.join(cwd, test_case)
    # simplex = Simplex2P()
    
    # simplex.read_data_file(file_path)
    # simplex.place_canonical_constraints()
    # simplex.two_phase()
    # print(simplex.flag)
    # if simplex.flag == 'Bounded solution':
    #     for i in simplex.solution:
    #         print("{0:.15f}".format(i), end=' ')
    # print()
    # print(time.time()-t0)

    # For uploading
    simplex = Simplex2P()
    simplex.read_data_console()
    simplex.place_canonical_constraints()
    simplex.two_phase()
    print(simplex.flag)
    if simplex.flag == 'Bounded solution':
        for i in simplex.solution:
            print("{0:.15f}".format(i), end=' ')
