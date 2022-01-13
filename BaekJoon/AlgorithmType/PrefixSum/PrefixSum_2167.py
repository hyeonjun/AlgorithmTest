"""
arr
1 2  4
8 16 32
누적합 ps
0  0  0  0
0  1  3  7
0  9  27 63
ps[i][j] = arr[i][j] + ps[i-1][j] + ps[i][j-1] - ps[i-1][j-1]

1,1 - 2,3 => 2,3
1,3 - 2,3 => 63 - 27 + 0 = 36
arr[x1][y1]~arr[x2][y2] 합 = ps[x2][y2] - ps[x2][y1-1] - ps[x1-1][y2] + ps[x1-1][y1-1]
"""
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
ps = [[0 for _ in range(m+1)] for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, m+1):
        ps[i][j] = arr[i-1][j-1] + ps[i-1][j] + ps[i][j-1] - ps[i-1][j-1]

for _ in range(int(input())):
    x1, y1, x2, y2 = map(int, input().split())
    print(ps[x2][y2] - ps[x2][y1-1] - ps[x1-1][y2] + ps[x1-1][y1-1])