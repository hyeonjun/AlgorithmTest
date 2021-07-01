# 보너스 점수
def solution(n, string):
    bonus = 0
    answer = 0
    for i in range(len(string)):
        if string[i] == "X":
            bonus = 0
        else:
            answer += (i+1)+bonus
            bonus += 1
            # asnwer, bonus = score+i+1+bonus, bonus+1
    return answer

print(solution(8, "XOOOXOOX"))