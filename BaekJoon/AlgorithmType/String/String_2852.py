answer = [0, 0]
score = 0
allTime = 48 * 60
for _ in range(int(input())):
    team, time = input().split()
    m, s = map(int, time.split(':'))
    print(time, score, answer)
    if team == '1':
        if score == 0: # 1번팀이 이기는 순간
            answer[0] += allTime - (60 * m + s)
        score += 1
        if score == 0: # 비기는 순간
            if answer[1] > 0:
                answer[1] = answer[1] - (allTime - (60 * m + s))
    else:
        if score == 0: # 2번팀이 이기는 순간
            answer[1] += allTime - (60 * m + s)
        score -= 1
        if score == 0: # 비기는 순간
            if answer[0] > 0:
                answer[0] = answer[0] - (allTime - (60 * m + s))
    print(time, score, answer)

print('{0:02d}:{1:02d}'.format(answer[0]//60, answer[0]%60))
print('{0:02d}:{1:02d}'.format(answer[1]//60, answer[1]%60))
