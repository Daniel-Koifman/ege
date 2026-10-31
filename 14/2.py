ch = (4 *2187 ** 2101 + 729 **2000 - 5 * 243**2100+ 81 **2200 - 3 * 27**2250 - 26244)
res = []
while ch > 0:
    res.append(ch % 27)
    ch = ch // 27
count = 0
for i in range(len(res)):
    if res[i] > 9:
        count += 1
print(count)