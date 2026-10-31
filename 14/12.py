ch = 5 * 729 ** 120 + 2 * 243 ** 80 - 7 * 81 ** 100 + 27 ** 150 - 3 * 9 ** 160 - 2026
res = []
while ch > 0:
    res.append(ch%27)
    ch = ch // 27
count = 0
for i in range(len(res)):
    if res[i] > 8:
        count += 1
print(count)