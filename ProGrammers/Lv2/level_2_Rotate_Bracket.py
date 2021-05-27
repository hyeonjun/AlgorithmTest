def solution(s):
    def isCheck(s):
        stack = []
        for i in s:
            if i == '(' or i == '{' or i == '[':
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                data = stack.pop()
                if (i == ']' and data != '[') or (i == '}' and data != '{') or (i == ')' and data != '('):
                    return False
        return True if len(stack) == 0 else False
    count = 0
    s = list(s)
    if len(s) % 2 != 0:
        return 0
    for i in range(len(s)):
        if isCheck(s):
            count += 1
        s.append(s.pop(0))
    return count

print(solution("[](){}")) # 3
print(solution("}]()[{")) # 2
print(solution("[)(]")) # 0
print(solution("}}}")) # 0