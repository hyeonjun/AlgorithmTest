# visited로 방문 체크를 해주었으나 추의 최대 무게가 200,000으로 상당히 시간이 오래 걸린 듯 함.
# 892ms
n = int(input())
arr = sorted(map(int, input().split()))
candi = set()
visited = [[0 for _ in range((n * arr[-1])+1)] for _ in range(n+1)]
def dfs(idx, w):
    if w not in candi:
        candi.add(w)
    if idx == n:
        return

    if not visited[idx][w]:
        for i in range(idx, n):
            for x in (1, 0, -1):
                visited[i][w] = 1
                dfs(i+1, abs(w + (arr[i] * x)))

dfs(0, 0)
print(sum(arr) - len(candi) + 1)

# =======================================================================

# 체크하지 않고 dfs를 진행하면서 가능한 수들을 한번에 저장하도록 함
# 784ms
n = int(input())
arr = list(map(int, input().split()))
candi = set()
def dfs(idx, w):
    if idx == n:
        return

    for i in range(idx, n):
        candi.update([w, w+arr[i], abs(w-arr[i])])
        dfs(i+1, w + arr[i])
        dfs(i+1, abs(w - arr[i]))

dfs(0, 0)
print(sum(arr) - len(candi) + 1)

# =======================================================================

# dfs를 사용하지 않고 루프를 돌면서 지금까지 확인된 숫자들에 대해 직접 계산하면서 가능한 수를 넣음
# 236ms로 가장 빠르다
n = int(input())
arr = list(map(int,input().split()))
ans = {arr[0]}
for i in range(1, n):
    temp = [arr[i]]
    for a in ans:
        temp += [a + arr[i], abs(a-arr[i])]
    ans.update(temp)
length = len(ans)
if 0 in ans:
    length -= 1
print(sum(arr) - length)