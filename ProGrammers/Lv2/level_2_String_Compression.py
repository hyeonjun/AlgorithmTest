def solution(s):
    answer = 1000

    def split(s, n):
        checker = s[:n]
        count = 0
        for i in range(0, len(s), n):
            if checker[-n:] == s[i:i + n]:
                count += 1
            else:
                if count == 1:
                    checker += s[i:i + n]
                else:
                    checker += str(count) + s[i:i + n]
                count = 1
        if count != 1:
            checker += str(count)
        return len(checker)
    if len(s) <= 1:
        return 1
    else:
        for i in range(1, len(s)):
            comp = split(s, i)
            answer = comp if answer >= comp else answer
    return answer

print(solution("aabbaccc")) # 7
print(solution("ababcdcdababcdcd")) # 9
print(solution("abcabcdede")) # 8
print(solution("abcabcabcabcdededededede")) # 14
print(solution("xababcdcdababcdcd")) # 17