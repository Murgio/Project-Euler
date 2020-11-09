import numpy as np

def largest(digits : int = 3):
    arr = np.arange(10**(digits-1), 10**digits, 1)
    matrix = np.triu(np.outer(arr, arr), k=0)
    mask = np.vectorize(lambda n: str(n) == str(n)[::-1])(matrix)
    return np.amax(matrix[mask])

print(largest())
