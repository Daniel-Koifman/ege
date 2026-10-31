from functools import *
@lru_cache()
def game(kucha, hod):
    if kucha <= 65 and hod == 2:
        return 1
    if kucha > 65 and hod == 2:
        return 0
    if kucha <= 65 and hod < 2:
        return 0
    if kucha > 65 and hod < 2:
        if hod == 0:
            return game(kucha - 3, hod + 1) and game(kucha - 5, hod + 1) and game(kucha // 4, hod + 1)
        if hod == 1:
            return game(kucha - 3, hod + 1) or game(kucha - 5, hod + 1) or game(kucha // 4, hod + 1)

for s in range(66, 100_000):
    if game(s, 0):
        print(s)
        break