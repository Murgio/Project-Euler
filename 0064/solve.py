from math import log, sqrt
from tqdm import tqdm

def squares(n: int) -> list:
    not_square = [True] * (n+1) 
    not_square[1] = False
    for i in range(2, int(n**0.5)+1):
        if not_square[i]:
            for j in range(1, int(log(n, i))+1):
                j = int(j**0.5)
                not_square[i**(2**j)] = False
    return not_square

N = 10_000

def sol(n: int = 10_000):
    odd = 0
    for i in tqdm(range(2, n+1)):
        if not sqrt(i).is_integer():
            a0, _ = divmod(r:=sqrt(i), 1)
            z = 0
            a = int(a0)
            while a / a0 != 2:
                a, _ = divmod(r:=1/(r-a), 1)
                a = int(a)
                z += 1
            odd += (z % 2 == 1)
    return odd

print(sol(n=N))
