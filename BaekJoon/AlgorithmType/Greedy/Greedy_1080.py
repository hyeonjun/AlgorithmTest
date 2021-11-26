n, m = map(int, input().split())
A = [list(map(int, input())) for _ in range(n)]
B = [list(map(int, input())) for _ in range(n)]

def reverse(x, y):
    for a in range(x, x+3):
        for b in range(y, y+3):
            A[a][b] = 1 - A[a][b]

flag = True
count = 0
for i in range(n-2):
    for j in range(m-2):
        if A[i][j] != B[i][j]:
            reverse(i, j)
            count += 1

for i in range(n):
    for j in range(m):
        if A[i][j] != B[i][j]:
            flag = False
            break
if flag:
    print(count)
else:
    print(-1)