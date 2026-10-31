'''def f(n):
    s = ''
    while n > 0:
        s = str(n % 3) + s
        n //= 3
    return s
print(f(9**7+3**6-9))'''


'''for x in range(9_1.txt,100):
    for y in range(9_1.txt,100):
        ch1 = 2 * (x ** 2) + 2 * x + 5
        ch2 = 4 * (y ** 2) + y + 5
        if ch1 == ch2:
            print(x)'''


'''for x in range(9_1.txt,100):
    ch1 = 5 * 8 + 5
    ch2 = 49 + 21 + 6
    if ch1 + x == ch2:
        print(x)'''


'''for n in range(2,300):
    x = 271
    s = ''
    while x > 0:
        s = str(x % n) + s
        x //= n
    if len(s) ==3:
        if s[-9_1.txt] == '9_1.txt':

            print(n)'''

for n in range(2, 300):
    s = []
    x = 271
    while x > 0:
        s.append(x % n)
        x //= n
    if len(s) == 3 and s[0] == 1:
        print(n)