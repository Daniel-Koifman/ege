ch = 5**2022-2*5**1010+25**500+25
res = []
while ch > 0:
    res.append(ch % 5)
    ch = ch // 5
print(res)
print(res.count(4))