def solution(new_id):
    import re
    new_id = re.sub('[^\w\-\_\.]', '', new_id.lower())
    new_id = re.sub('\.+', '.', new_id)
    new_id = re.sub('^\.|\.$', '', new_id)
    if len(new_id) == 0:
        new_id = "a"
    if len(new_id) >= 16:
        new_id = re.sub('\.$', '', new_id[:15])
    if len(new_id) < 3:
        new_id = new_id + new_id[-1] * (3 - len(new_id))
    return new_id

print(solution("...!@BaT#*..y.abcdefghijklm"))
print(solution(	"z-+.^."))
print(solution("=.="))
print(solution(	"123_.def"))
print(solution("abcdefghijklmn.p"))