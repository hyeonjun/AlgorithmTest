def solution(s):
    answer = 0
    def isCheck(data):
        return True if data == data[::-1] else False
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            if isCheck(s[i:j]) and (answer < len(s[i:j])):
                answer = len(s[i:j])
    return answer

print(solution("abcdcba")) # 7
print(solution("abacde")) # 3
