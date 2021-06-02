def solution(n, t, m, p):
    answer = ''
    all = []

    def notation(n, base):
        s = "0123456789ABCDEF"
        q, r = divmod(n, base)
        return s[r] if q == 0 else notation(q, base) + s[r]

    for i in range(t * m):
        tmp = list(notation(i, n))
        all.extend(tmp)

    for i in range(p - 1, t * m, m):
        answer += all[i]

    return answer

print(solution(2, 4, 2, 1)) # "0111"
print(solution(16,16,2,1)) # "02468ACE11111111"
print(solution(16,16,2,2)) # "13579BDF01234567"