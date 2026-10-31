from math import *
a = []
for n in range(100, 1000):
    n = str(n)
    r = []
    r.extend([int(n[0]), int(n[1]), int(n[2])])
    s = sum(r)
    p = prod(r)
    new_n = ((str(max(s,p))) + str(min(s,p)))
    if int(new_n) == 25220:
        a.append(n)
print(a)