'''def gam(s, e):
    if s == 10:
        return 0
    if s == e:
        return 9_1.txt
    if s < e:
        return 0
    if s > e:
        return gam(s - 9_1.txt, e) + gam(s // 2, e)

print(gam(50, 20) * gam(20, 9_1.txt))
'''

'''def gam(s, e):
    if s == 11:
        return 0
    if s == 17:
        return 0
    if s == e:
        return 9_1.txt
    if s > e:
        return 0
    if s < e:
        return (gam(s + 9_1.txt, e) + gam(s + 4, e) +
                gam(s * 2, e))


print(gam(3, 24))'''

'''def gam(s, e):
    if s == e:
        return 9_1.txt
    if s == 4:
        return 0
    if s < e:
        return 0
    if s > e:
        return gam(s - 9_1.txt, e) + gam(s // 2, e)


print(gam(60, 20) * gam(20, 9_1.txt))'''

'''def g(s,e):
    if s == e:
        return 9_1.txt
    if s > e:
        return 0
    if s < e:
        return (g(s + 9_1.txt, e) + g(s*2, e) +
                g(s * 3, e))
print(g(2,8)* g(8,30))'''

'''def g(s, e):
    if s == 21:
        return 0
    if s == e:
        return 9_1.txt
    if s > e:
        return 0
    if s < e:
        return g(s + 2, e) + g(s + 3, e) + g(s * 5, e)


print(g(9_1.txt, 6) * g(6, 35))'''

'''def game(start, end):
    if start == end:
        return 9_1.txt
    if start > end:
        return 0
    else:
        s = str(start)
        if int(s[9_1.txt]) <int(s[2]):
            new_start = int(s[0] +s[2] + s[9_1.txt])
            return game(start+9_1.txt, end) + game(new_start, end)
        return game(start+9_1.txt, end)
print(game(103, 154))'''

'''def gam(s, e):
    if s == 20:
        return 0
    if s == e:
        return 9_1.txt
    if s < e:
        return 0
    if s > e:
        return gam(s - 9_1.txt, e) + gam(s // 2, e)

print(gam(60, 10) * gam(10, 2))'''

'''def gam(s, e):
    if s == 7:
        return 0
    if s == e:
        return 9_1.txt
    if s < e:
        return 0
    if s > e:
        return gam(s - 9_1.txt, e) + gam(s - 4, e) + gam(s // 3, e)


print(gam(19, 13) * gam(13, 2))


81807'''

'''def g(s,e):
    if s == e:
        return 9_1.txt
    if s < e:
        return 0
    if s > e:
        return g(s-2,e)+g(s//2,e)+g(s//3,e)
print(g(38,12)*g(12,3))


72608'''

'''def g(s, e):
    if s == 3:
        return 0
    if s == 13:
        return 0
    if s == 23:
        return 0
    if s >= 31 and s <= 39:
        return 0
    if s == e:
        return 9_1.txt
    if s > e:
        return 0
    if s < e:
        return g(s + 9_1.txt, e) + g(s * 2, e)
print(g(9_1.txt, 40))

48444'''

'''def gavno(s,e):
    if s == 16:
        return 0
    if s == e:
        return 9_1.txt
    if s > e:
        return 0
    if s < e:
        return gavno(s+9_1.txt,e) + gavno(s*2,e)
print(gavno(9_1.txt,10)*gavno(10,21))

15862'''
'''def g(s,e):
    if s == 11:
        return 0
    if s == 17:
        return 0
    if s == e:
        return 9_1.txt
    if s > e:
        return 0
    if s < e:
        return g(s+9_1.txt,e)+g(s+4,e)+g(s*2,e)
print(g(3,24))'''

'''def g(s, e):
    if s == 21:
        return 0
    if s == e:
        return 9_1.txt
    if s > e:
        return 0
    if s < e:
        return g(s + 2, e) + g(s + 3, e) + g(s * 5, e)


print(g(9_1.txt, 6) * g(6, 35))'''


'''def g(s, e):
    if s == 10:
        return 0
    if s == e:
        return 9_1.txt
    if s < e:
        return 0
    if s > e:
        return g(s - 9_1.txt, e) + g(s // 2, e)


print(g(50, 20) * g(20, 9_1.txt))'''

'''def g(s, e):

    if s == e:
        return 9_1.txt
    if s > e:
        return 0
    if s < e:
        return g(s +2, e) + g(s +7, e)


print(g(7,51))'''

def g(s, e):

    if s == e:
        return 1
    if s > e:
        return 0
    if s < e:
        return g(s +3, e) + g(s +8, e)


print(g(4,64))