from functools import *
@lru_cache()
def game(kucha, hod):
    if kucha <= 71 and (hod == 4 or hod == 2):
        return 1
    if kucha > 71 and hod == 4:
        return 0
    if kucha <= 71 and hod == 4:
        return 0
    if kucha > 71 and hod < 4:
        if hod == 0:
            return game(kucha - 3, hod + 1) and game(kucha - 5, hod + 1) and game(kucha // 4, hod + 1)
        if hod == 1:
            return game(kucha - 3, hod + 1) or game(kucha - 5, hod + 1) or game(kucha // 4, hod + 1)
        if hod == 2:
            return game(kucha - 3, hod + 1) and game(kucha - 5, hod + 1) and game(kucha // 4, hod + 1)
        if hod == 3:
            return game(kucha - 3, hod + 1) or game(kucha - 5, hod + 1) or game(kucha // 4, hod + 1)

def game2(kucha, hod):
    if kucha <= 71 and hod == 2:
        return 1
    if kucha > 71 and hod == 2:
        return 0
    if kucha <= 71 and hod < 2:
        return 0
    if kucha > 71 and hod < 2:
        if hod == 0:
            return game2(kucha - 3, hod + 1) and game2(kucha - 5, hod + 1) and game2(kucha // 4, hod + 1)
        if hod == 1:
            return game2(kucha - 3, hod + 1) or game2(kucha - 5, hod + 1) or game2(kucha // 4, hod + 1)

for s in range(72, 100000):
    if game(s, 0):
        print(s)


print('- - - - - - - - - -')

for s1 in range(72, 100000):
    if game2(s1, 0):
        print(s1)
