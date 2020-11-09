from tqdm import tqdm
def chain(n):
    if n == 1:
        return 1
    if n % 2 == 0:
        return 1 + chain(n/2)
    return 1 + chain(3*n+1)

def sol(limit: int):
    m = 0
    num = 1
    for i in tqdm(range(1, limit)):
        c = chain(i)
        if c > m:
            m = c
            num = i
    return num

print(sol(int(1e6)))
