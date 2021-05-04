def solution(s):
    if len(s) not in [4, 6]:
        return False
    import re
    answer = re.search('[a-zA-Z]', s)
    return True if answer == None else False

print(solution("a234"))
print(solution("123456789"))
print(solution("1234"))

def solution(s):
    return s.isdigit() and len(s) in [4, 6]

print(solution("a234"))
print(solution("123456789"))
print(solution("1234"))
