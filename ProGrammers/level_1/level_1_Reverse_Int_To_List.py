def solution(n):
    return [int(i) for i in str(n)][::-1]

print(solution(12345))