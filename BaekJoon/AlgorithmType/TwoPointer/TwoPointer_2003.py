# 투 포인터
n, m = map(int, input().split())
arr = list(map(int, input().split()))
answer = 0
sumV = arr[0]
start, end = 0, 1
while start <= end <= n:
    if sumV == m:
        answer += 1
        end += 1
        if end <= n:
            sumV += arr[end-1]
    elif sumV < m:
        end += 1
        if end <= n:
            sumV += arr[end-1]
    else:
        sumV -= arr[start]
        start += 1
print(answer)

# 구간합
n, m = map(int, input().split())
arr = list(map(int, input().split()))

prefix = [0 for _ in range(n+1)]
for i in range(1, n+1):
    prefix[i] = arr[i-1] + prefix[i-1]

answer = 0

start, end = 1, 1
while end <= n:
    value = prefix[end] - prefix[start-1]
    if value == m:
        answer += 1
        end += 1
    elif value < m:
        end += 1
    else:
        start += 1

    if start > end:
        start, end = end, start
print(answer)