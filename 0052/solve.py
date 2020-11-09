def check_perm(num1, num2):
    arr = [0] * 20
    while num1 > 0:
        arr[num1%10] += 1
        num1 //= 10
    while num2 > 0:
        arr[num2%10] -= 1
        num2 //= 10
    return not any(arr)

def sol(upto: int):
    n = 100
    while True:
        current_num = n
        i = 2
        while check_perm(current_num, i*current_num):
            if i == upto:
                return current_num
            i += 1
        n += 1

print(sol(upto=6))
