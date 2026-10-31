k = 0
for s in open('3.txt'):
    a = list(map(int, s.split()))
    ch = [a.count(i) for i in a]
    if ch.count(4) == 4 and ch.count(1) == 3:
        sp = sum(a[i] for i in range(len(a)) if ch[i] == 4)
        snp = [a[i] for i in range(len(a)) if ch[i] == 1]
        if sum(snp) / len(snp) > sp:
            k += 1
print(k)
