def solution(str1, str2):
    answer = 0
    s1 = []
    s2 = []
    for x, y in zip(str1, str1[1:]):
        if (x + y).isalpha():
            s1.append((x + y).lower())
    for x, y in zip(str2, str2[1:]):
        if (x + y).isalpha():
            s2.append((x + y).lower())

    intersection = len([s1.remove(x) for x in s2 if x in s1]) if len(s1) > len(s2) else \
        len([s2.remove(x) for x in s1 if x in s2])

    union = s1 + s2
    try:
        return int(intersection / len(union) * 65536)
    except:
        return 65536

print(solution("FRANCE", "french")) # 16384
print(solution("handshake", "shake hands")) # 65536
print(solution("aa1+aa2", "AAAA12")) # 43690
print(solution("E=M*C^2", "e=m*c^2")) # 65536