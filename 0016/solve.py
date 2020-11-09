def sol(n: int = 2**1000):
    s = 0
    for i in str(n):
        s += int(i)
    return s
print(sol())
