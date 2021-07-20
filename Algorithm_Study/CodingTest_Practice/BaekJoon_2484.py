"""
같은 눈이 4개가 나오면 50,000원+(같은 눈)×5,000원의 상금을 받게 된다.
같은 눈이 3개만 나오면 10,000원+(3개가 나온 눈)×1,000원의 상금을 받게 된다.
같은 눈이 2개씩 두 쌍이 나오는 경우에는 2,000원+(2개가 나온 눈)×500원+(또 다른 2개가 나온 눈)×500원의 상금을 받게 된다.
같은 눈이 2개만 나오는 경우에는 1,000원+(같은 눈)×100원의 상금을 받게 된다.
모두 다른 눈이 나오는 경우에는 (그 중 가장 큰 눈)×100원의 상금을 받게 된다.
"""
def solution(dice):
    answer = [0 for _ in range(len(dice))]
    for i in range(len(dice)):
        tmp = sorted(dice[i])
        if len(set(tmp)) == 1:
            answer[i] = 50000 + tmp[0] * 5000
        elif len(set(tmp)) == 2:
            if tmp[1] == tmp[2]:
                answer[i] = 10000 + tmp[1] * 1000
            else:
                answer[i] = 2000 + (tmp[1]+tmp[2]) * 500
        elif len(set(tmp)) == 3:
            if tmp[0] == tmp[1]:
                answer[i] = 1000 + tmp[0] * 100
            elif tmp[2] == tmp[3]:
                answer[i] = 1000 + tmp[3] * 100
        else:
            answer[i] = max(tmp) * 100
    return max(answer)

dice = [
    [3, 3, 3, 3],
    [3, 3, 6, 3],
    [2, 2, 6, 6],
    [6, 2, 1, 5]]
print(solution(dice))