from itertools import combinations as combs
from tqdm import tqdm

def prime_gen(n):
    # sieve of erastothenes
    primes = [True] * (n+1)
    primes[0], primes[1] = False, False
    for i in range(2, int(n**0.5)+1):
        if primes[i]:
            for j in range(i*i, n+1, i):
                primes[j] = False
    return primes

C = prime_gen(int(3e4))
P = [i for i in range(3, len(C)) if C[i]]

BIG_C = prime_gen(int(1e8))
BIG_P = [i for i in range(3, len(BIG_C)) if BIG_C[i]]

PS = set(BIG_P)

def in_primes(*args) -> bool:
    string = lambda num1, num2: int(str(num1)+str(num2)) in PS and int(str(num2)+str(num1)) in PS
    return all(string(*c) for c in combs(args, 2))

def go_over(arr):
    new_arr = []
    for c in tqdm(arr):
        for i in range(1, len(P)):
            if P[i] not in c:
                merged = set(list(c)+[P[i]])
                if in_primes(*merged):
                    new_arr.append(set(merged))
    return new_arr

def sol(ps : int = 5):
    global P, PS, BIG_P
    #print(P)
    two_cands = []
    for c in tqdm(combs(P, 2)):
        if in_primes(*c):
            two_cands.append(set(c))

    old_arr = two_cands[:]
    print(old_arr)
    for i in range(3, ps+1):
        if i == 5:
            print(old_arr)
        print(i)
        arr = go_over(old_arr)
        old_arr = arr[:]
	min_s = float("inf")
	for t in arr:
		min_s = min(min_s, sum(t))
    return min_s

print(sol())

