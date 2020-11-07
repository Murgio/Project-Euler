def sol(n: int):
    s = 0
    is_prime = lambda x: sum(x % i == 0 for i in range(2, int(x**0.5)+1)) == 0
    for i in range(2, n):
        if is_prime(i):
            s += i
    return s

print(sol(10))
print(sol(int(2e6)))
