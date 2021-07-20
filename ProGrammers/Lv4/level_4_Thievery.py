def solution(money):
    dp1 = [0 for _ in range(len(money))]
    dp2 = [0 for _ in range(len(money))]

    # 1번 집을 터는 경우
    dp1[0] = money[0]
    for i in range(1, len(money) - 1):  # 마지막 집은 인접해있기 때문에 털지 못함
        dp1[i] = max(dp1[i - 1], dp1[i - 2] + money[i])
    # 1번 집을 털지 않는 경우
    for i in range(1, len(money)):
        dp2[i] = max(dp2[i - 1], dp2[i - 2] + money[i])

    return max(dp1[-2], dp2[-1])

print(solution([1, 2, 3, 1])) # 4