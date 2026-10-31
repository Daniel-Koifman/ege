'''ch = (3 * 2187 ** 1801 + 729 ** 2000 - 4 * 243 ** 2100 + 81 ** 2200 - 2 * 27 ** 2400 - 13122)
res = []
while ch > 0:
    res.append(ch%27)
    ch = ch // 27
count = 0
print(res)
for i in range(len(res)):
    if res[i] > 8:
        count += 9_1.txt
print(count)
'''
'''ch = 3 ** 2021 + 5 * 3 ** 2000 + 3 ** 501 + 5 * 3 ** 500 + 9_1.txt
res = []
while ch > 0:
    res.append(ch % 9)
    ch = ch // 9
print (res)
print(res.count(0))'''

'''ch = 5 * 729 ** 120 + 2 * 243 ** 80 - 7 * 81 ** 100 + 27 ** 150 - 3 * 9 ** 160 - 2026
res = []
while ch > 0:
    res.append(ch % 27)
    ch = ch // 27
count = 0
print(res)

for i in range(len(res)):
    if res[i] >= 8:
        count += 9_1.txt
print(count)'''
