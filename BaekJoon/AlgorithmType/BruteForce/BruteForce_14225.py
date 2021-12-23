n = int(input())
s = list(map(int, input().split()))
answer = set()

def dfs(idx, num):
    if idx == n:
        answer.add(num)
        return
    dfs(idx+1, num)
    dfs(idx+1, num+s[idx])
dfs(0, 0)
for i in range(1, 2000000):
    if i not in answer:
        print(i)
        break
