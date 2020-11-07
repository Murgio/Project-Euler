from tqdm import tqdm

def primes(n: int = 20):
    is_prime = lambda x: sum(x % i == 0 for i in range(2, int(x**0.5)+1)) == 0
    return list(filter(is_prime, range(2, n+1)))

def solve(n: int = 20):
    ps = primes(n=n)
    b_l = 1
    for i in ps:
        b_l *= i
    b_u = 1
    for i in range(2, n+1):
        b_u *= i
    smallest = b_u

    for i in tqdm(range(b_l, b_u+1)):
        if all(i % j == 0 for j in range(2, n+1)):
            smallest = min(smallest, i)
            if smallest != b_u:
                return smallest
    return smallest

print(solve(n=20))
