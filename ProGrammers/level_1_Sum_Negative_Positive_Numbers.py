def solution(absolutes, signs):
    answer = 0
    for i in range(len(absolutes)):
        answer = answer + absolutes[i] if signs[i] else answer - absolutes[i]
    return answer

print(solution([4,7,12], [True,False,True]))
print(solution([1,2,3], [False,False,True]))

def solution(absolutes, signs):
    return sum(absolutes[i] * (1 if signs[i] > 0 else -1) for i in range(len(absolutes)))

print(solution([4,7,12], [True,False,True]))
print(solution([1,2,3], [False,False,True]))