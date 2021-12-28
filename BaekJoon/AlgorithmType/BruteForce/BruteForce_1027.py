"""
- 기울기
가까운 건물부터 기울기를 계산해서 이전의 기울기보다
크면 볼 수 있는 건물 수를 더하면 된다.
"""
n = int(input())
arr = list(map(int, input().split()))

answer = [0 for _ in range(n)]
for i in range(n):
    gradient_right = -1e9
    result = 0
    for j in range(i+1, n):
        tmp = (arr[j] - arr[i]) / (j-i)
        if gradient_right < tmp:
            gradient_right = tmp
            answer[i] += 1
    gradient_left = 1e9
    for j in range(i-1, -1, -1):
        tmp = (arr[i] - arr[j]) / (i-j)
        if gradient_left > tmp:
            gradient_left = tmp
            answer[i] += 1
print(max(answer))

# ===========================================

answer = [0 for _ in range(n)]
for i in range(n):
    gradient = -1e9
    for j in range(i+1, n):
        tmp = (arr[j] - arr[i]) / (j - i)
        if gradient < tmp:
            gradient = tmp
            answer[i] += 1
            answer[j] += 1
print(max(answer))