from collections import defaultdict
n, d, k, c = map(int, input().split())
arr = [int(input()) for _ in range(n)]
arr *= 2 # 원형이므로 계산을 편하게 하기 위해서

count = defaultdict(int)
for i in range(k):
    count[arr[i]] += 1
count[c] += 1

left, right = 0, k
answer = 0

while right < n*2:
    answer = max(answer, len(count))

    count[arr[left]] -= 1
    if count[arr[left]] == 0:
        del count[arr[left]]
    count[arr[right]] += 1

    left += 1
    right += 1
print(answer)