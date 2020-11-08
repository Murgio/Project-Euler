from itertools import permutations as p

def sol(n: int):
    d = "0123456789"
    for index, num in enumerate(p(d), 1):
        if index == n:
            return "".join(num)
print(sol(int(1e6)))

