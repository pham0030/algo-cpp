import os
# using minisat to solve the problem
os.system("minisat tmp.cnf tmp.sat")

with open("tmp.sat", "r") as satfile:
    for line in satfile:
        if line.split()[0] == "UNSAT":
            print("There is no solution")
        elif line.split()[0] == "SAT":
            pass
        else:
            print(line)