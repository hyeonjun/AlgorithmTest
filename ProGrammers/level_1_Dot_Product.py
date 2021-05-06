def solution(a, b):
    answer = sum(list(map(lambda x,y: x*y, a, b)))
    return answer

print(solution([1,2,3,4], [-3,-1,0,2]))
print(solution([-1,0,1], [1,0,-1]))