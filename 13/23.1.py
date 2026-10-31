def f(n):
    if n == 154:
        return 1
    if n > 154:
        return 0

    c = f(n + 1)
    if (n // 10) % 10 < n % 10:
        с += f(n // 100 * 100 + n % 10 * 10 + n // 10 % 10)
    return c
print(f(101))