from tqdm import tqdm
from itertools import combinations as combs

def prime_gen(n: int) -> list:
    arr = [True] * (n+1)
    arr[0] = False
    arr[1] = False
    for i in range(2, int(n**0.5)+1):
        if arr[i]:
            for j in range(i*i, n+1, i):
                arr[j] = False
    return arr

N = int(1e6)
C = prime_gen(N)
P = [str(i) for i in range(2, N+1) if C[i]]
PS = set(P)

def replace(string, perm, num):
    s = list(string[:])
    for p in perm:
        s[p] = num
    return "".join(s)

def sol(z: int) -> str:
    global P, PS
    #cache = dict()
    for i in tqdm(range(len(P))):
        digits = len(P[i])
        for j in range(1, digits):
            perms = combs(range(digits), j)
            for p in perms:
                fam = 0
                consider = False
                sol = []
                for n in range(0, 10):
                    s = replace(P[i], p, str(n))
                    contains = (r := str(int(s))) in PS
                    if P[i] == r:
                        consider = True
                        continue
                    if contains:
                        sol.append(r)
                        fam += 1
                if consider and fam+1 == z:
                    print((P[i]), p, fam)

print(sol(z=8))
