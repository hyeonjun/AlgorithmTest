"""
3 * 3
11 12 13     1  2  3
21 22 23 =>  2  4  6
31 32 33     3  6  9
"""
n = int(input())
k = int(input())
left, right = 1, k

while left <= right:
    mid = (left+right) // 2 # 배열 B의 값

    cnt = 0 # 배열 A의 값 중 mid 보다 작은 값들 계산
    for i in range(1, n+1): # 행별로 계산
        cnt += min(mid // i, n) # mid//i가 n을 벗어나면 해당 행의 n 열 모두 mid보다 작은 값이다
    # 작은 값의 개수를 구했을 때 k와 같으면서 가장 최소인 mid값을 구해야한다.
    if cnt < k:
        left = mid+1
    else:
        right = mid-1
print(left)
