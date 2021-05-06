def solution(d, budget):
    answer = 0
    d.sort()
    tmp = 0
    for i in range(len(d)):
        tmp += d[i]
        if tmp <= budget:
            answer+=1
    return answer

print(solution([1,3,2,5,4],9))
print(solution([2,2,3,3],10))