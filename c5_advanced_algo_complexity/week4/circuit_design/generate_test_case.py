import random
V = 100000
C = 100000

random.seed(1)
allow_values = list(range(-V, V+1))
allow_values.remove(0)
with open('V100k.case', 'w') as f:
    f.write(str(V) + " " + str(C) + "\n")
    for i in range(C):
        l1 = random.choice(allow_values)
        l2 = random.choice(allow_values)
        f.write(str(l1) + " " + str(l2) + "\n")
