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
print(game(110, 154))'''

def g (s,e):
    if s == e:
        return 1
    if s > e:
        return 0
    if s < e:
        return g(s+1,e)+g(s*2,e)+g(s*3,e)
print(g(3,9)*g(9,30))