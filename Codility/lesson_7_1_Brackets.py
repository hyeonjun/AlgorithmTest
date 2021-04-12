def solution(S): # 87%
    if len(S) == 0:
        return 1
    check = ""
    try:
        for i in S:
            if (i == "{") or (i == "[") or (i == "("):
                check += i
            if i == ")":
                if check[-1] == "(":
                    check = check[:-1]
                else:
                    return 0
            if i == "]":
                if check[-1] == "[":
                    check = check[:-1]
                else:
                    return 0
            if i == "}":
                if check[-1] == "{":
                    check = check[:-1]
                else:
                    return 0
    except:
        return 0

    if len(check) == 0:
        return 1
    else:
        return 0

print(solution("{[()()]}"))
print(solution("([)()]"))
print(solution(")("))
print(solution("{{{{"))


def SideSolution(S):
    # write your code in Python 3.6

    stack = []
    for bracket in S:
        if bracket == '{' or bracket == '[' or bracket == '(':
            stack.append(bracket)
        else:
            if len(stack) == 0:
                return 0
            item = stack.pop()
            if item == '{':
                if bracket != '}':
                    return 0
            elif item == '[':
                if bracket != ']':
                    return 0
            else:
                if bracket != ')':
                    return 0

    if len(stack) > 0:
        return 0

    return 1

print(SideSolution("{[()()]}"))
print(SideSolution("([)()]"))
print(SideSolution(")("))
print(SideSolution("{{{{"))