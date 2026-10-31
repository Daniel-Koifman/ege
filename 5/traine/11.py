a = []
for n in range(1000, 10_000):
    s = str(n)
    r = []
    r.extend([int(s[0]), int(s[1]), int(s[2]), int(s[3])])
    s = sum(r)
    m = max(r)
    N = min(r)
    p1 = s - m
    p2 = s - N
    l = (str(max(p1, p2))+str(min(p1, p2)))
    if int(l) == 2018:
        a.append(n)
print(min(a))