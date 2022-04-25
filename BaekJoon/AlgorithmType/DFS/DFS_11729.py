n = int(input())

# start: 현재 n개의 원판이 쌓어있는 위치
# end: start에서 옮길 위치
# via: start에서 end로 옮기기 위해 거치는 곳
def dfs(n, start, end, via): # a, c, b
    if n == 1:
        print(start, end)
        return
    dfs(n-1, start, via, end) # a에서 c를 거쳐서 b로
    print(start, end)# a의 1개 남은 원판을 a에서 c로 옮김
    dfs(n-1, via, end, start)# b에서 a를 거쳐서 c로 옮겨 끝

# 하노이의 총 횟수는 2^n -1이다
print(2 ** n - 1)
dfs(n, 1, 3, 2)

# ====================================================

n = int(input())
def dfs(n, start, end, via):
    if n == 1:
        return [[start, end]]
    return dfs(n-1, start, via, end) + [[start, end]] + dfs(n-1, via, end, start)

print(2 ** n - 1)
for x, y in dfs(n, 1, 3, 2):
    print(x, y)