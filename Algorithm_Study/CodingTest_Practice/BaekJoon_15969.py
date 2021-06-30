# 행복
def solution(n, score):
    return max(score) - min(score)

print(solution(5, [27, 35, 92, 75, 42])) # 65
print(solution(8, [85, 42, 79, 95, 37, 11, 72, 32])) # 84