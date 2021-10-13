n, m = list(map(int, input().split()))
num = [] # m개의 수열을 저장할 리스트

def dfs(start):
    if len(num) == m:
        print(' '.join(map(str, num)))
        return
    
    for i in range(start, n+1):
        num.append(i)
        dfs(i)
        num.pop()
dfs(1)