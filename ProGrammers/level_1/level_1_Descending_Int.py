def solution(n):
    return int("".join(sorted([i for i in str(n)], reverse=True)))

print(solution(118372))

def solution(n):
    return int("".join(sorted(str(n), reverse=True)))

print(solution(118372))