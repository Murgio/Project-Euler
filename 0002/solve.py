def fib():
    s = 0
    a, b = 1, 1
    while a+b <= int(4e6):
        if (a+b) % 2 == 0:
            s += (a+b)
        a, b = b, a+b
    return s

s = fib()
print(s)
