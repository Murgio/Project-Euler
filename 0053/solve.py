import math

def sol(n: int = 100):
    # [1, n]
    p = 0
    for r in range(1, n+1):
        for n in range(r, n+1):
            p += math.comb(n, r) > 1e6
    return p

print(sol(n=100))
