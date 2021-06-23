def solution(sticker):
    if len(sticker) < 4:
        return max(sticker)
    dp1, dp2 = [0] * len(sticker), [0] * len(sticker)

    # 맨 앞 스티커를 땔 때
    dp1[0] = dp1[1] = sticker[0]
    # 1, -1 인덱스는 사용하지 못하므로
    for i in range(2, len(sticker) - 1):
        dp1[i] = max(dp1[i - 1], dp1[i - 2] + sticker[i])

    # 맨 앞 스티커를 때지 않을 때
    dp2[0] = 0
    dp2[1] = sticker[1]
    for i in range(2, len(sticker)):
        dp2[i] = max(dp2[i - 1], dp2[i - 2] + sticker[i])
    return max(dp1[-2], dp2[-1])

print(solution([14, 6, 5, 11, 3, 9, 2, 10])) # 36
print(solution([1, 3, 2, 5, 4])) # 8