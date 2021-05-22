def solution(p):
    def split(w):
        u = 0
        v = 0
        for i in range(len(w)):
            if w[i] == "(":
                u += 1
            else:
                v += 1
            if u == v:
                return w[:i + 1], w[i + 1:]

    def isCheck(w):
        bracket = []
        for i in w:
            if i == "(":
                bracket.append(i)
            else:
                if len(bracket) == 0:
                    return False
                bracket.pop()
        return False if len(bracket) > 0 else True

    answer = ''

    if len(p) == 0:
        return ""
    u, v = split(p)
    if isCheck(u):
        return u + solution(v)
    else:
        answer += "("
        answer += solution(v)
        answer += ")"

        for i in u[1:-1]:
            answer += ")" if i == "(" else "("

    return answer

print(solution("(()())()")) # "(()())()"
print(solution(")(")) # "()"
print(solution("()))((()")) # "()(())()"