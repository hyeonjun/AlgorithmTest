def solution(S):
    stack = []

    for i in S:
        if i == "(":
            stack.append(i)
        else:
            if len(stack) == 0:
                return 0
            stack.pop()
    return 0 if len(stack) > 0 else 1

print(solution("(()(())())"))
print(solution("())"))

