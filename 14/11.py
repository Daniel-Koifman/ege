ch = 1331**650 - 55*11**510+77*11**100-3*11**50-221
res =  []
while ch > 0:
    res.append(ch%11)
    ch = ch // 11
count = 0
print(res)
print(res.count(10))