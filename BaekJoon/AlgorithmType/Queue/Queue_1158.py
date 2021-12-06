"""
1 2 3 4 5 6 7
4 5 6 7 1 2       3
7 1 2 4 5         6
4 5 7 1           2
1 4 5             7
1 4               5
                  1 4
"""
n, k = map(int, input().split())
num = [i for i in range(1, n+1)]
answer = []
idx = 0
for _ in range(n):
    idx += k-1
    if idx >= len(num):
        idx %= len(num)
    answer.append(str(num.pop(idx)))
print("<", ", ".join(answer), ">", sep="")