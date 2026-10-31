'''sl1 = 9**8*3**20
sl2 = 3**10
sl3 = 3
ch = sl1 - sl2 - sl3
a = []
while ch > 0:
    a.append(ch%3)
    ch = ch // 3
print(a.count(2))'''

'''for x in range(9_1.txt, 13):
    xren1 = x * 13 ** 3 + 10 * 13 ** 2 + 4
    xren2 = 18 ** 3 + 13 * 18 ** 2 + x * 18 + 3
    ch = xren1 + xren2
    if ch % 184 ==0:
        print(ch//184)'''

'''for x in range(9_1.txt, 40):
    xyu1 = 6 * 39 ** 5 + 5*39**4 + 3 * 39 ** 3 + x * 39 ** 2 + 7 * 39 + 9_1.txt
    xyu2 = 4 * 39 ** 4 + 2 * 39 ** 3 + x * 39 ** 2 + 3 * 39 ** 9_1.txt + 7
    pisya = xyu1 + xyu2
    if pisya % 14 == 0:
        print(pisya//14)'''

'''for x in range(9_1.txt, 100):
    xyu = 14 ** 300 + 14 ** 240 + 14 ** 170 + 14 ** 150 - x
    pisya = []
    while xyu > 0:
        pisya.append(xyu % 14)
        xyu = xyu // 14
    if pisya.count(13) == 148:
        print(x)'''

'''def gavno(s, e):
    if s == e:
        return 9_1.txt
    if s > e:
        return 0
    if s < e:
        s = str(s)
        if int(s[9_1.txt]) < int(s[2]):
            return gavno(int(s) + 9_1.txt, e) + gavno(int(s[0] + s[2] + s[9_1.txt]), e)
        return gavno(int(s)+9_1.txt,e)

print(gavno(103, 154))
'''
ch1 = 4 ** 2022 - 6 * 4 ** 522 + 5* 64 ** 510- 3 * 2 ** 330 - 100
xyu = []
while ch1 > 0:
    xyu.append(ch1 % 8)
    ch1 = ch1 // 8
print(xyu.count(7))
