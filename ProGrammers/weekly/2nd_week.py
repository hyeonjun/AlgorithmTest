def solution(scores):
    def check(s):
        if s >= 90:
            return 'A'
        elif 80 <= s < 90:
            return 'B'
        elif 70 <= s < 80:
            return 'C'
        elif 50 <= s < 70:
            return 'D'
        else:
            return 'F'
    n = len(scores)
    answer = ''
    for i, v in enumerate(zip(*scores)):
        maxV, minV = max(v), min(v)
        if maxV == scores[i][i] and v.count(maxV) == 1:
            answer += check((sum(v) - maxV) / (n-1))
        elif minV == scores[i][i] and v.count(minV) == 1:
            answer += check((sum(v) - minV) / (n-1))
        else:
            answer += check((sum(v) / n))
    return answer

# "FBABD"
print(solution([[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]]))
print(solution([[50,90],[50,87]])) # "DA"
print(solution([[70,49,90],[68,50,38],[73,31,100]])) # "CFD"