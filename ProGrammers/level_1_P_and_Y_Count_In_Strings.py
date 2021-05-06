def solution(s):
    p = y = 0
    for i in s.lower():
        if i == 'p': p+=1
        elif i == 'y' : y+=1
    return True if p ==y else False

print(solution("pPoooyY"))
print(solution("Pyy"))

def solution(s):
    return s.lower().count('p') == s.lower().count('y')

print(solution("pPoooyY"))
print(solution("Pyy"))