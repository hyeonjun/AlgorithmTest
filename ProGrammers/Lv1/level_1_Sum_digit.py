def solution(n):
    answer = 0
    n = [i for i in str(n)]
    for i in n:
        answer+=int(i)
    return answer

print(solution(123))
print(solution(456))

def solution(n):
    return sum([int(i) for i in str(n)])

print(solution(123))
print(solution(456))