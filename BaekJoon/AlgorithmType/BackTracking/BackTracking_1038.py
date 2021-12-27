"""
0 1 2 3 4 5 6 7 8 9 10 20 21 30 31 32 40 41 42 43 ...
"""
n = int(input())
if n < 10:
    print(n)
else:
    answer, idx = 0, 9
    def dfs(depth, limit, num):
        global answer, idx
        if depth == limit:
            idx += 1
            if idx == n:
                answer = num
                return
        for i in range(int(num[-1])):
            dfs(depth+1, limit, num+str(i))
    for i in range(1, 11):
        for j in range(1, 10):
            dfs(0, i, str(j))
    print(answer if answer != 0 else -1)