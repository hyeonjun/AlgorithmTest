def solution(s):
    data = []
    for i in range(len(s)):
        if len(data) > 0 and data[-1] == s[i]:
            data.pop()
        else:
            data.append(s[i])
    return 1 if len(data) == 0 else 0

print(solution("baabaa"))
print(solution("cdcd"))