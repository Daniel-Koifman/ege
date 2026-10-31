from itertools import*
countsl = 0
countch = 0
for p in product('АГЕИЛНРТ', repeat = 5):
    s = ''.join(p)
    countsl += 1
    if (countsl %2 == 1 and s[0] != 'Т' and
            (s.count('Н') == 1 or s.count('Н') == 2)):
        countch += 1
print(countch)

