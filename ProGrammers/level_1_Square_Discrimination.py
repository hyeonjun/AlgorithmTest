def solution(n):
    return (int(n**0.5) +1)**2 if int(n**0.5) **2 == n else -1

print(solution(121))
print(solution(3))