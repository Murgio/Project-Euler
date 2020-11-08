from tqdm import tqdm

L = lambda n, a, b: n**2+a*n+b
def is_prime(n):
    return sum(n%i==0 for i in range(2, int(n**0.5)+1)) == 0

def sol():
    res_a, res_b = 0, 0
    bs = list(filter(is_prime, range(2, 1000)))
    m = 0
    print(len(bs))
    for b in bs:
        for a in tqdm(range(-999, 1000, 1)):
            n = 0
            while L(n, a, b) > 0 and is_prime(L(n, a, b)):
                n += 1
                if n > m:
                    m = n
                    res_a = a
                    res_b = b
    return res_a, res_b

print(sol())

