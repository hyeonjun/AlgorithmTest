from itertools import permutations
n = int(input())
innings = [list(map(int, input().split())) for _ in range(n)]
orders = permutations(list(range(1, 9)), 8)

def baseball(order):
    score = 0
    idx = 0
    for inning in innings:
        out = 3
        b1, b2, b3 = 0, 0, 0 # 1루, 2루, 3루
        while out:
            if inning[order[idx]] == 0: # 아웃
                out -= 1
            elif inning[order[idx]] == 1: # 안타
                score += b3
                b1, b2, b3 = 1, b1, b2
            elif inning[order[idx]] == 2: # 2루타
                score += b2 + b3
                b1, b2, b3 = 0, 1, b1
            elif inning[order[idx]] == 3: # 3루타
                score += b1 + b2 + b3
                b1, b2, b3 = 0, 0, 1
            elif inning[order[idx]] == 4: # 홈런
                score += b1 + b2 + b3 + 1
                b1, b2, b3 = 0, 0, 0
            idx = (idx+1) % 9
    return score

answer = -1
for tmp in orders:
    tmp = list(tmp)
    # 아인타는 자신이 가장 좋아하는 선수인 1번 선수를 4번 타자로 미리 결정했다.
    answer = max(answer, baseball(tmp[:3] + [0] + tmp[3:]))
print(answer)