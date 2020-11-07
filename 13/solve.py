with open("large_nums.txt", "r") as f:
    nums = list(map(int, f.read().splitlines()))
    print(str(sum(nums))[:10])
