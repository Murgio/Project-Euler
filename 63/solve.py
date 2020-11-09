def sol():
    s = 0
    for n in range(1, 130):
        for x in range(1, 10):
            if 10**(n-1) <= x**n < 10**n:
                s += 1
    return s
print(sol())

