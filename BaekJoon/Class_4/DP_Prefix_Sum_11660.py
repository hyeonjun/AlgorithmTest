"""
prefix_sum = [[A A B B B]
              [A A B B B]
              [C C D D D]
              [C C D D D]]

(3,3)~(4,5)까지의 합을 구하는 예시 = D에 속한 수들의 합
prefix_sum[4][5] = A~D를 모두 더한 값.
여기에서 각 A,B,C를 빼면 D의 값이 남는다
prefix_sum[2][5] = A + B
prefix_sum[4][2] = A + C
A + B + C + D - A - B - A - C = D - A
prefix_sum[2][2] = A
D - A + prefix_sum[2][2] = D

=> (x1, y1) ~ (x2, y2)의 합 =
            prefix_sum[x2][y2] - prefix_sum[x1-1][y2] - prefix_sum[x2][y1-1] + prefix_sum[x1-1][y1-1]
"""
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
matrix = [list(map(int ,input().split())) for _ in range(n)]
prefix_sum = [[0 for _ in range(n+1)] for _ in range(n+1)]

for i in range(n):
    for j in range(n): # 왼쪽 위쪽 더하기
        prefix_sum[i+1][j+1] = prefix_sum[i][j+1] + prefix_sum[i+1][j] - prefix_sum[i][j] + matrix[i][j]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    print(prefix_sum[x2][y2] - prefix_sum[x1-1][y2] - prefix_sum[x2][y1-1] + prefix_sum[x1-1][y1-1])