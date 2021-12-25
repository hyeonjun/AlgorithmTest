import math
n, k = map(int, input().split())
arr = list(map(int, input().split()))
answer = 1e9

def rmse(target):
    result = 0
    avg = sum(target) / len(target)
    for t in target:
        result += (t-avg) ** 2
    return math.sqrt(result/len(target))

for i in range(n-k+1):
    for j in range(n-k+1-i):
        tmp = arr[i:i+k+j]
        answer = min(answer, rmse(tmp))
print(answer)