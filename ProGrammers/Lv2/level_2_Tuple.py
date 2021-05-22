from collections import Counter
def solution(s):
    import re
    s = re.findall('\d+', s)
    checker = {}
    for i in s:
        n = int(i)
        if n in checker:
            checker[n] += 1
        else:
            checker[n] = 1
    checker = sorted(checker.items(), key=lambda x: x[1], reverse=True)

    return [i[0] for i in checker]

print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}")) # [2,1,3,4]
print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}")) # [2,1,3,4]
print(solution("{{20,111},{111}}")) # [111,20]
print(solution("{{123}}")) # [123]
print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}")) # [3,2,4,1]

def solution(s):
    import re
    from collections import Counter
    s = Counter(re.findall('\d+', s))  # 위에서 dict에 넣는 과정과 같음
    return [int(i[0]) for i in sorted(s.items(), key=lambda x:x[1], reverse=True)]

print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}")) # [2,1,3,4]
print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}")) # [2,1,3,4]
print(solution("{{20,111},{111}}")) # [111,20]
print(solution("{{123}}")) # [123]
print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}")) # [3,2,4,1]
