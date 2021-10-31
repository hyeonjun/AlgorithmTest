"""
1 - -1
2 - 1 (2)
3 - -1
4 - 2 (2, 2)
5 - 1 (5)
6 - 3 (2, 2, 2)
7 - 2 (2, 5)

13 - 5, 5 x, 5, 2, 2, 2, 2
"""

n = int(input())
if n == 1 or n == 3:
    print(-1)
else:
    q1, r = n // 5, n % 5
    if r % 2 == 0:
        print(q1+r//2)
    else:
        q1 -= 1
        r += 5
        print(q1+r//2)