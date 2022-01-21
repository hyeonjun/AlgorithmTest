# 카카오 2022 블라인드 4번
def solution(n, info):
    global answer, result
    answer = []
    result = 0
    def calcScore(ryan):
        score = 0
        for i in range(11):
            if ryan[i] == info[i] == 0:
                continue
            if ryan[i] > info[i]:
                score += 10 - i
            else:
                score -= 10 - i
        return score

    def dfs(idx, cnt, ryan):
        global answer, result
        if idx == -1 and cnt: # 끝까지 다 갔는데 화살을 덜 쐈으면
            return
        if cnt == 0:
            score = calcScore(ryan)
            if result < score:
                result = score
                answer = ryan[:]
            return
        for arrow in range(cnt, -1, -1): # 점수 배점이 낮은 것부터 많이 맞춘것 중 점수 차가 가장 큰 것
            ryan[idx] = arrow
            dfs(idx-1, cnt-arrow, ryan)
            ryan[idx] = 0
    # 라이언이 가장 큰 점수차로 이길 수 있는 경우가 여러 가지일 때,
    # 가장 낮은 점수를 더 많이 맞힌 경우를 return 해야한다
    # 그래서 점수 배점이 가장 맞은 0점인 10번 과녁부터 계산한다
    dfs(10, n, [0 for _ in range(11)])
    return answer if result != 0 else [-1]

print(solution(5, [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]))
print(solution(9, [0, 0, 1, 2, 0, 1, 1, 1, 1, 1, 1]))
print(solution(10, [0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 3]))