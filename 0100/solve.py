import math

def sol(n: int):
    # solve eq with Wolfram over integers
    eq = lambda x: 0.5*(math.sqrt(8*x*x-8*x+1)+1)
    x = 1_000_000_000
    while True:
        y = eq(x)
        if y.is_integer() and y > n:
            return x
        if x % int(1e6) == 0:
            print(x)
        x += 1

print(sol(int(1e12)))
