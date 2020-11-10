def sol():
    s = 0
    a = [1, -2, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1]
    day = 0
    for y in range(1900, 2001):
        for m in range(len(a)):
            if day == 6 and y != 1900:
                s += 1
            month = a[m]
            if y % 4 == 0 and y != 1900 and m == 1:
                month += 1
            month += 30
            day = ((month % 7 + 1) + day) % 7
    return s

print(sol())
