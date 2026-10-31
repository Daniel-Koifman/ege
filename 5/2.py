r = []
for k in range(1000, 10_000):
    k = str(k)
    a = []
    a.extend([int(k[0]), int(k[1]), int(k[2]), int(k[3])])
    s = sum(a)
    m = max(a)
    n = min(a)
    p1 = s - m
    p2 = s - n
    l = str(max(p1, p2)) + str(min(p1, p2))
    if int(l) == 2013:
        r.append(k)
print(min(r))

