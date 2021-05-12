def solution(dartResult):
    import re
    tmp = re.split('([SDT*#]+)', dartResult)
    tmp = list(filter(lambda x: x != '', tmp))
    answer = [0] * len(tmp)
    print(tmp)
    def calc(n, s):
        if s == 'S':
            return int(n) ** 1
        elif s == 'D':
            return int(n) ** 2
        elif s == 'T':
            return int(n) ** 3

    for i in range(0, len(tmp), 2):
        if len(tmp[i + 1]) > 1:
            value = calc(tmp[i], tmp[i + 1][0])
            if tmp[i + 1][1] == '*':
                if i != 0:
                    answer[i - 2] = answer[i - 2] * 2
                answer[i] = value * 2
            elif tmp[i + 1][1] == '#':
                answer[i] = value * (-1)
        else:
            value = calc(tmp[i], tmp[i + 1])
            answer[i] = value
    return sum(answer)

# print(solution("1S2D*3T"))
# print(solution("1D2S#10S"))
# print(solution("1D2S0T"))
# print(solution("1S*2T*3S"))
# print(solution("1D#2S*3S"))
# print(solution("1T2D3D#"))
print(solution("1D2S3T*"))

def solution(dartResult):
    bonus = {'S' : 1, 'D' : 2, 'T' : 3}
    option = {'' : 1, '*' : 2, '#' : -1}
    import re
    # [('1', 'D', ''), ('2', 'S', ''), ('3', 'T', '*')]
    dart = re.findall('(\d+)([SDT])([*#]?)', dartResult)
    print(dart)
    for i in range(len(dart)):
        if dart[i][2] == '*' and i > 0:
            dart[i-1] *= option[dart[i][2]]
        dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]
    return sum(dart)

print(solution("1D2S3T*"))