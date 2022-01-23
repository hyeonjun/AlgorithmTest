n, k = map(int, input().split())
arr = list(map(int, input().split()))
tmp = sum(arr[:k])
answer = tmp
for i in range(n-k):
    tmp = tmp - arr[i] + arr[k+i]
    answer = max(tmp, answer)
print(answer)
