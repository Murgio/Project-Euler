N = 600851475143

T = 13195

def is_prime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def largest_factor(n):
    factors = []
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            factors.append(i)
    return max(filter(is_prime, factors))
print(largest_factor(T))
print(largest_factor(N))
