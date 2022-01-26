n, m = map(int, input().split())
arr = [list(map(int, list(input()))) for _ in range(n)]
k = int(input())

answer = 0

for i in range(n):
    zero = arr[i].count(0)

    ### 조건 ###
    # 1. 0의 개수가 k보다 작거나 같아야 해당 행을 켜지게 할 수 있다.
    # 2. k가 짝수면 0 개수도 짝수, k가 홀수면 0 개수도 홀수이어야 해당 행을 켜지게 할 수 있다.
    if zero <= k and k % 2 == zero % 2:
        # 해당 행과 같은 행
        result = 0
        for j in range(n):
            if arr[i] == arr[j]:
                result += 1
        answer = max(answer, result)
print(answer)