ans = 0
for num, s in enumerate(open('4.txt'), 1):
    a = list(map(int, s.split()))
    ch = [a.count(i) for i in a]
    if ch.count(2) == 6 and ch.count(1) == 2:
        p = [a[i] for i in range(len(a)) if ch[i] == 2]
        np = [a[i] for i in range(len(a)) if ch[i] == 1]
        if (max(p) - min(p)) ** 2 > 2 * sum(x ** 2 for x in np):
            ans = num
print(ans)
