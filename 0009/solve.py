import math
from tqdm import tqdm

def sol(s: int = 1000):
    for i in tqdm(range(1, s)):
        for j in range(i+1, s):
            c = math.sqrt(i**2 + j**2) 
            if c % 1 == 0 and s-i-j-c == 0:
                return i*j*c
print(sol(s=1000))
