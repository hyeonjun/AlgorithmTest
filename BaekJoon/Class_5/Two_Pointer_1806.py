import sys
input = sys.stdin.readline
n, s = map(int, input().split())
num = list(map(int, input().split()))

# 투 포인터
start, end, cur = 0, 0, 0
answer = 1e9
while True:
    if cur >= s:
        answer = min(answer, end-start)
        cur -= num[start]
        start += 1
    elif end == n:
        break
    else:
        cur += num[end]
        end += 1
print(answer if answer != 1e9 else 0)

# 부분합
start, end = 0, 1
prefix_sum = [0 for _ in range(n+1)]
for i in range(1, n+1):
    prefix_sum[i] = prefix_sum[i-1] + num[i-1]
answer = 1e9
while start < n:
    if prefix_sum[end] - prefix_sum[start] >= s:
        answer = min(answer, end-start)
        start += 1
    else:
        if end < n:
            end += 1
        else:
            start += 1
print(answer if answer != 1e9 else 0)