def solution(n):
    answer = []
    for i in range(1, n+1):
        if n % i == 0:
            answer.append(i)
    return sum(answer)

print(solution(15))

def solution(n):
    return sum([i for i in range(1, n//2+1) if n % i == 0]+[n])

print(solution(15))