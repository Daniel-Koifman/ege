for x in range(2735, 0, -1):
    ch = (5**2025+5**1500-x)
    res=[]
    while ch >0:
        res.append(ch%5)
        ch = ch//5
    count = 0
    for i in range(len(res)):
        if res[i] ==0:
            count += 1
    if count == 527:
        print(x)
        exit()