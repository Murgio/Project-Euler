with open("matrix.txt", "r") as f:
    M = f.read().splitlines()
    M = [[int(i) for i in row.split(",")] for row in M]

MT = [[131, 673, 234, 103, 18],
      [201, 96, 342, 965, 150],
      [630, 803, 746, 422, 111],
      [537, 699, 497, 121, 956], 
      [805, 732, 524, 37, 331]]

def sol(M):
    for i in range(len(M)):
        for j in range(len(M[0])):
            if i == 0 and j == 0:
                continue
            else:
                M[i][j] += min(M[i-1][j] * (i >= 1) or float("inf"),
                               M[i][j-1] * (j >= 1) or float("inf"))
    return M[-1][-1]

print(sol(M))

