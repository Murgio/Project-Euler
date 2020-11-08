def sol(end=1001*1001):
    s = 1
    start = 1
    for i in range(1, 100000000):
        arr = [2*i] * 4
        for a in arr:
            s += start + a
            start += a
            if start == end:
                return s

print(sol())
