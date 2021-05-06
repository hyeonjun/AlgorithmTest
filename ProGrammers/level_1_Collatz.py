def solution(num):
    answer = 0
    while num > 1:
        q, n = divmod(num, 2)
        num = q if n == 0 else num * 3 +1
        answer+=1
        if answer == 500:
            return -1
    return answer

print(solution(6))
print(solution(16))
print(solution(626331))