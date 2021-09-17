def solution(weights, head2head):
    # 승률, 자신보다 몸무게가 무거운 복서를 이긴 횟수, 몸무게가 무거운 복서, 작은 번호
    info = []
    for i, v in enumerate(weights):
        win, lose, win_heavy = 0, 0, 0
        data = head2head[i]
        for j in range(len(data)):
            if data[j] == 'W':
                win += 1
                if weights[i] < weights[j]:
                    win_heavy += 1
            elif data[j] == 'L':
                lose += 1
            else:
                pass
        win_rate = win / (win + lose) * 100 if win > 0 else 0
        info.append([win_rate, win_heavy, v, i])
    info.sort(reverse=True, key=lambda x:(x[0], x[1], x[2], -x[3]))
    return list(i[-1]+1 for i in info)
print(solution([50,82,75,120], ["NLWL","WNLL","LWNW","WWLN"])) # [3,4,1,2]
print(solution([145,92,86], ["NLW","WNL","LWN"])) # [2,3,1]
print(solution([60,70,60], ["NNN","NNN","NNN"])) # [2,1,3]