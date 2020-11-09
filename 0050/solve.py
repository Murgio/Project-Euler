from tqdm import tqdm
is_prime = lambda n: sum(n%i==0 for i in range(2, int(n**0.5)+1)) == 0

def primes():
    for i in range(2, 200_000):
        if is_prime(i):
            yield i

def sol():
    ps = list(primes())
    num_ps = 0
    prime = 2

    for i in range(len(ps)):
        s = ps[i]
        local_ps = 0
        while s < 1e6:
            for p in tqdm(ps[i+1:]):
                s += p
                local_ps += 1
                if is_prime(s):
                    if local_ps > num_ps:
                        num_ps = local_ps
                        prime = s
                if s >= 1e6:
                    break
            if len(ps[i+1:]) < 21:
                break
    return prime

print(sol())

