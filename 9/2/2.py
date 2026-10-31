k = 0
for s in open('2.txt'):
    a, b, c = map(int, s.split())
    s1, s2, s3 = a * b, b * c, a * c
    if s1 + s2 > s3 and s1 + s3 > s2 and s2 + s3 > s1:
        k += 1
print(k)
