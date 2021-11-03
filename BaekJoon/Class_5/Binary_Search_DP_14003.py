"""
bisect 함수 : 이진 탐색을 쉽게 구현하게끔 해주는 함수, 정렬된 배열에서 특정 원소 찾기

from bisect import bisect_left, bisect_right
nums = [0,1,2,3,4,5,6,7,8,9]
n = 5
print(bisect_left(nums, n)) # 5
print(bisect_right(nums, n)) # 6

bisect_left(a, x) : 정렬된 순서를 유지하면서 리스트 a에 데이터 x 삽입할 때 가장 왼쪽 인덱스 찾기
bisect_right(a, x) : 정렬된 순서를 유지하면서 리스트 a에 데이터 x 삽입할 때가장 오른쪽 인덱스 찾기
"""
def binary_search(lst, x):
    left, right = 0, len(lst)
    while left < right:
        mid = (left + right) // 2
        if lst[mid] < x:
            left = mid+1
        else:
            right = mid
    return left # 삽입시킬 위치를 반환
n = int(input())
arr = [0] + list(map(int, input().split()))
cmp = [-(1e9+1)]
maxVal = 0
dp =[0 for _ in range(n+1)]
for i in range(1, n+1):
    if cmp[-1] < arr[i]:
        cmp.append(arr[i])
        dp[i] = len(cmp) -1
        maxVal = dp[i]
    else:
        dp[i] = binary_search(cmp, arr[i])
        cmp[dp[i]] = arr[i]

print(maxVal)
answer = []
for i in range(n, 0, -1):
    if maxVal == dp[i]:
        answer.append(arr[i])
        maxVal -= 1
print(*answer[::-1])


#=========================================================================
# bisect 활용
from bisect import bisect_left
n = int(input())
arr = [0] + list(map(int, input().split()))
dp = [0 for _ in range(n+1)]
cmp = [-(1e9+1)] # 이진탐색을 위해 생성
maxVal = 0

for i in range(1, n+1):
    if cmp[-1] < arr[i]: # 이진탐색으로 저장된 값들은 정렬되므로 맨 뒤의 값 비교
        cmp.append(arr[i])
        dp[i] = len(cmp)-1
        maxVal = dp[i]
    else:
        dp[i] = bisect_left(cmp, arr[i]) # 현재 값이 어느 위치의 값에 해당하는지 비교
        print('dp[i] : ', dp[i], 'arr[i] : ', arr[i])
        cmp[dp[i]] = arr[i]
    print(dp)
    print(cmp)
print(maxVal)

answer = []
for i in range(n, 0, -1):
    if maxVal == dp[i]:
        answer.append(arr[i])
        maxVal -= 1
print(*answer[::-1])
