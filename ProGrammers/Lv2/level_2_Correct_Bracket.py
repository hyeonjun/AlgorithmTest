def solution(s):
    bracket = []
    for i in s:
        if i == "(":
            bracket.append(i)
        else:
            if len(bracket) == 0:
                return False
            bracket.pop()
    return False if len(bracket) > 0 else True

print(solution("()()")) # True
print(solution("(())()")) # True
print(solution(")()(")) # False
print(solution("(()(")) # False