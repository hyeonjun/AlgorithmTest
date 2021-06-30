# 수빈이와 수열
def solution(n, seq):
    answer = [seq[0]]
    for i in range(1, n):
        answer.append(seq[i]*(i+1)-sum(answer))
    return answer


print(solution(1, [2])) # [2]
print(solution(4, [3, 2, 3, 5])) # [3, 1, 5, 11]
print(solution(5, [1, 2, 2, 3, 4])) # [1, 3, 2, 6, 8]