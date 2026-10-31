ch = 2 * 3 ** 2022 + 5 * 3 ** 1800 + 3 **1001 + 4 * 3 ** 1000 + 8
res = []
while ch > 0:
    res.append(ch % 9)
    ch = ch // 9
print(res)
print(res.count(0))