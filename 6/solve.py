def sol(n: int = 100):
    sum_squares = lambda k: k*(k+1)*(2*k+1)/6
    square_sum = lambda k: (k*(k+1)/2)**2
    return abs(sum_squares(n) - square_sum(n))

print(sol(100))
print(sol(10))
