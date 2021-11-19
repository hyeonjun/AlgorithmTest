# print('1' < '2') # True
# print('1' > '2') # False
k = int(input())
sign = input().split()
num = [i for i in range(10)]
visited = [False for _ in range(10)]
maxV, minV = "", ""
def check(i, j, op):
    if op == '<':
        return i < j
    if op == '>':
        return i > j

def dfs(depth, s):
    global maxV, minV
    if depth == k+1:
        if len(minV) == 0: # 가장 작은 값이므로 첫번째결과값이 minV다
            minV = s
        else:
            maxV = s
        return
    for i in range(10):
        if not visited[i]:
            if depth == 0 or check(s[-1], str(i), sign[depth-1]):
                visited[i] = True
                dfs(depth+1, s+str(i))
                visited[i] = False

dfs(0, "")
print(maxV)
print(minV)