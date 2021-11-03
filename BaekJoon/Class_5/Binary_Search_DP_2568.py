"""
a를 기준으로 정렬시켜서
b의 가장 긴 증가하는 부분 수열을 구함
전체 길이에서 부분 수열의 길이를 제거하면
없애야할 전기줄이 나옴

여기서 b의 가장 긴 증가하는 부분 수열을
이진 탐색을 사용하여 구함
"""
import sys
input = sys.stdin.readline

def binary_search(lst, x):
    left, right = 0, len(lst)
    while left < right:
        mid = (left + right) // 2
        if lst[mid] < x:
            left = mid + 1
        else:
            right = mid
    return left

n = int(input())
line = [list(map(int, input().strip().split())) for _ in range(n)]
line.sort(key=lambda x:x[0])
cmp = [-(1e9+1)]
maxVal = 0
dp = [0 for _ in range(n+1)]
for i in range(1, n+1):
    if cmp[-1] < line[i-1][1]:
        cmp.append(line[i-1][1])
        dp[i] = len(cmp)-1
        maxVal = dp[i]
    else:
        dp[i] = binary_search(cmp, line[i-1][1])
        cmp[dp[i]] = line[i-1][1]
print(n-maxVal)

no_answer = []
for i in range(n, 0, -1):
    if dp[i] == maxVal:
        no_answer.append(line[i-1])
        maxVal -= 1
    if maxVal == 0:
        break

answer = []
for i in line:
    if i not in no_answer:
        answer.append(i[0])

answer.sort()
for a in answer:
    print(a)
