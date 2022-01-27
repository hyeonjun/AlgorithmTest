n, m = map(int, input().split())
board = [[0 for _ in range(m+1)]]
for _ in range(n):
    board.append([0]+list(map(int, list(input()))))
prefix = [[0 for _ in range(m+1)] for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        prefix[i][j] = board[i][j] + prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1]

def SUM(x1, y1, x2, y2):
    return prefix[x2][y2] - prefix[x1-1][y2] - prefix[x2][y1-1] + prefix[x1-1][y1-1]

answer = 0

# 123
# 123
# 123
for i in range(1, m-1):
    for j in range(i+1, m):
        x = SUM(1, 1, n, i)
        y = SUM(1, i+1, n, j)
        z = SUM(1, j+1, n, m)
        answer = max(answer, x*y*z)

# 111
# 222
# 333
for i in range(1, n-1):
    for j in range(i+1, n):
        x = SUM(1, 1, i, m)
        y = SUM(i+1, 1, j, m)
        z = SUM(j+1, 1, n, m)
        answer = max(answer, x*y*z)

# 122
# 133
# 133
for i in range(1, m):
    for j in range(1, n):
        x = SUM(1, 1, n, i)
        y = SUM(1, i+1, j, m)
        z = SUM(j+1, i+1, n, m)
        answer = max(answer, x * y * z)

for i in range(1, n):
    for j in range(1, m):
        # 113
        # 223
        # 223
        x1 = SUM(1, 1, i, j)
        y1 = SUM(i + 1, 1, n, j)
        z1 = SUM(1, j + 1, n, m)

        # 111
        # 223
        # 223
        x2 = SUM(1, 1, i, m)
        y2 = SUM(i + 1, 1, n, j)
        z2 = SUM(i + 1, j + 1, n, m)

        # 112
        # 112
        # 333
        x3 = SUM(1, 1, i, j)
        y3 = SUM(1, j + 1, i, m)
        z3 = SUM(i + 1, 1, n, m)

        answer = max(answer, x1*y1*z1, x2*y2*z2, x3*y3*z3)

print(answer)


# # 113
# # 223
# # 223
# for i in range(1, n):
#     for j in range(1, m):
#         x = SUM(1, 1, i, j)
#         y = SUM(i+1, 1, n, j)
#         z = SUM(1, j+1, n, m)
#         answer = max(answer, x * y * z)
#
# # 111
# # 223
# # 223
# for i in range(1, n):
#     for j in range(1, m):
#         x = SUM(1, 1, i, m)
#         y = SUM(i+1, 1, n, j)
#         z = SUM(i+1, j+1, n, m)
#         answer = max(answer, x * y * z)
#
# # 112
# # 112
# # 333
# for i in range(1, n):
#     for j in range(1, m):
#         x = SUM(1, 1, i, j)
#         y = SUM(1, j+1, i, m)
#         z = SUM(i+1, 1, n, m)
#         answer = max(answer, x * y * z)