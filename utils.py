def prime_gen(n):
    # sieve of erastothenes
    primes = [True] * (n+1)
    primes[0], primes[1] = False, False
    for i in range(3, int(n**0.5)+1, 2):
        if primes[i]:
            for j in range(i*i, n+1, i):
                primes[j] = False
    return primes


