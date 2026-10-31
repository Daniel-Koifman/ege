ch = (5 * 512 ** 1000 + 256 ** 1001 - 128 ** 1002 + 64 ** 1003 - 7 * 32 ** 1004 - 5120)
res = []
while ch > 0:
    res.append(ch % 32)
    ch = ch // 32
count = 0
for i in range(len(res)):
    if res[i] <= 9:
        count += 1
print(count)
