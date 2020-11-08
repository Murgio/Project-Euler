def fib_gen():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b

def sol(num_digits: int = 3):
    num_ds = lambda n: len(str(n))
    for i, num in enumerate(fib_gen(), 1):
        if num_ds(num) == num_digits:
            return i

print(sol(1000))
