def nth_prime(n=10_001):
    last_prime = 2
    k = 0
    i = 2
    is_prime = lambda x: sum(x%i==0 for i in range(2, int(x**0.5)+1)) == 0
    while k < n:
        if is_prime(i):
            last_prime = i
            k += 1
        i += 1
    return last_prime


print(nth_prime())
