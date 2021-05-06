def solution(n):
    def notation(n, base):
        s = "0123456789ABCDEF"
        q = n//base
        r = n%base
        return s[r] if q==0 else notation(q,base)+s[r]
    answer = 0
    value = notation(n, 3)
    for i, v in enumerate(value):
        answer += int(v)*(3**i)
    return answer

print(solution(45))
print(solution(125))

def solution(n):
    tmp = ''
    while n:
        tmp += str(n%3)
        n = n//3
    answer = int(tmp, 3) # 3진법 -> 10진법
    return answer
print(solution(45))
print(solution(125))
