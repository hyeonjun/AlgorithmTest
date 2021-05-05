def solution(n):
    answer = ''
    s = ["수", "박"]
    for i in range(1,n+1):
        if i % 2 == 1:
            answer += s[0]
        else:
            answer += s[1]
    return answer

print(solution(3))
print(solution(4))

def solution(n):
    s = "수박" * n
    return s[:n]

print(solution(3))
print(solution(4))