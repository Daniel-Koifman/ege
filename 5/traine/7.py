a = []
for k in range(1000, 10000):
    k = str(k)
    jopa = []
    jopa.extend([int(k[0]), int(k[1]), int(k[2]), int(k[3])])
    s = sum(jopa)
    m = max(jopa)
    n = min(jopa)
    p1 = s - m
    p2 = s - n
    l = (str((max(p1, p2))) + str(min(p1, p2)))
    if int(l) == 2018:
        a.append(k)
print(min(a))
