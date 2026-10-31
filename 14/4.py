ch = (3*512**1500+256**1501-2*128**1502+64**1503-3*32**1504-10240)
res=[]
while ch > 0:
    res.append(ch%32)
    ch = ch//32
count = 0
for i in range(len(res)):
    if res[i] <= 9:
        count += 1
print(count)