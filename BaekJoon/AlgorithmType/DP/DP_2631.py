"""
가장 긴 부분수열 길이 = 순서를 바꾸지 않아도 되는 아이들
"""

n = int(input())
num = [0]+[int(input()) for _ in range(n)]
dp = [0 for _ in range(n+1)]
cmp = [-1e9]
maxLeng = 0

def binary(lst, x):
    left, right = 0, len(lst)
    while left < right:
        mid = (left+right) // 2
        if lst[mid] < x:
            left = mid+1
        else:
            right = mid
    return left

for i in range(1, n+1):
    if cmp[-1] < num[i]:
        cmp.append(num[i])
        dp[i] = len(cmp)-1
        maxLeng = dp[i]
    else:
        dp[i] = binary(cmp, num[i])
        cmp[dp[i]] = num[i]
print(n-maxLeng)