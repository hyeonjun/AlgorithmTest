# 200 ms
n = int(input())
num = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())
maxV, minV = -1e9, 1e9
def dfs(idx, answer, add, sub, mul, div):
    global maxV, minV
    if idx == n:
        maxV = max(maxV, answer)
        minV = min(minV, answer)
        return
    if add > 0:
        dfs(idx+1, answer+num[idx], add-1, sub, mul, div)
    if sub > 0:
        dfs(idx+1, answer-num[idx], add, sub-1, mul, div)
    if mul > 0:
        dfs(idx+1, answer*num[idx], add, sub, mul-1, div)
    if div > 0:
        dfs(idx+1, int(answer/num[idx]), add, sub, mul, div-1)

dfs(1, num[0], add, sub, mul, div)
print(maxV)
print(minV)

# ========================================================
# 424ms
n = int(input())
num = list(map(int, input().split()))
op = list(map(int, input().split()))
sign = ['+', '-', '*', '/']
maxV, minV = -1e9, 1e9
result = []
def dfs():
    global maxV, minV
    if len(result) == n-1:
        tmp = num[0]
        for i in range(n-1):
            if result[i] == '+':
                tmp += num[i+1]
            if result[i] == '-':
                tmp -= num[i+1]
            if result[i] == '*':
                tmp *= num[i+1]
            if result[i] == '/':
                tmp = int(tmp/num[i+1])
        maxV = max(maxV, tmp)
        minV = min(minV, tmp)
        return

    for i in range(len(sign)):
        if op[i] > 0:
            result.append(sign[i])
            op[i] -= 1
            dfs()
            op[i] += 1
            result.pop()
dfs()
print(maxV)
print(minV)