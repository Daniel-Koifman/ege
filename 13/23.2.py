def f(s, e):
    if s == e:
        return 1
    if s > e:
        return 0
    if str(s) [-2] < str(s) [-1]:
        return f(s + 1, e) + f(int(str(s)[-3] + str(s)[-1] + str(s)[-2]), e)
    return f(s + 1, e)
print(f(101, 154))