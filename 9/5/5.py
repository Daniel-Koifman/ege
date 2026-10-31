k = 0
for s in open('5.txt'):
    a = list(map(int, s.split()))
    ch = [a.count(i) for i in a]
    if ch.count(3) == 3 and ch.count(1) == 3:
        sp = sum(a[i] for i in range(len(a)) if ch[i] == 3)
        snp = sum(a[i] for i in range(len(a)) if ch[i] == 1)
        if sp ** 2 > snp ** 2:
            k += 1
print(k)
