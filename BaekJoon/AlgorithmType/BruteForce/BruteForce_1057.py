"""
          1                          2
    1           2     |       3              4
 1     2  |  3     4  |  5       6   |   7       8
1 2 | 3 4 | 5 6 | 7 8 | 9 10 | 11 12 | 13 14 | 15 16
"""
n, i, j = map(int, input().split())
answer = 0
while i != j:
    i -= i //2
    j -= j //2
    answer += 1
print(answer)