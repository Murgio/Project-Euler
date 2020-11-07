from tqdm import tqdm

def num_div(n: int):
    num = 0
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            num += 2
    return num
assert num_div(28) == 6

def triangle_num_gen():
    i = 1
    s = 0
    while True:
        s += i
        yield s
        i += 1


def sol(t: int = 500):
    # > t
    for n in tqdm(triangle_num_gen()):
        a = num_div(n)
        if a % 10 == 0:
            print(a)
        if a > t:
            return n
print(sol(t=500))
