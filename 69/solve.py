from tqdm import tqdm

N = int(1e6)

phi_N = [0] * (N+1)

def gcd(n, m):
    while (r := divmod(n, m)[1]) != 0:
        n, m = max(r, m), min(r, m)
    return m

def phi(n):
    global phi_N, N
    p = 1
    coprime = []
    if a := phi_N[n]:
        return a
    for i in range(2, n):
        if (d := gcd(n, i)) == 1:
            p += 1
            coprime.append([n, i])
    phi_N[n] = p
    for a, b in coprime:
        # phi(n) is a multiplicative function
        if a*b <= N:
            phi_N[a*b] = p * phi_N[b]
    return p

def slow(n: int):
    # find argmax(n/phi(n))
    val = 2
    max_frac = 1
    # [2;n]
    for i in tqdm(range(2, n+1)):
        fr = i/phi(i)
        if fr > max_frac:
            max_frac = fr
            val = i
    return val

# *********************************************

def prime_gen(n):
    # sieve of erastothenes
    primes = [True] * (n+1)
    primes[0], primes[1] = False, False
    for i in range(2, int(n**0.5)+1):
        if primes[i]:
            for j in range(i*i, n+1, i):
                primes[j] = False
    return primes

C = prime_gen(N)

def dist_prime_factors(n: int) -> list:
    return [i for i in range(2, int(n**0.5)+1) if C[i] and n % i == 0]

def phi_fast(n):
    phi = 1
    for p in dist_prime_factors(n):
        phi *= (1-1/p)
    return phi*n

def fast(n: int):
    # insight:
    # phi(n) = n(1-1/p_1)(1-1(p_2))...(1-1/p_r) where p_1...p_3 are distinct prime factors
    val = 2
    max_frac = 1
    for i in tqdm(range(2, n+1)):
        fr = i/phi_fast(i)
        if fr > max_frac:
            max_frac = fr
            val = i
    return val

print(fast(n=N))
