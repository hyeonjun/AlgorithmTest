def solution(phone_number):
    return "*" * (len(phone_number) - 4) + phone_number[-4:]

print(solution("0106249273"))

def solution(p):
    import re
    return re.sub(r'\d(?=\d{4})', "*", p)

print(solution("0106249273"))