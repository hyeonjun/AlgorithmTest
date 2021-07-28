# 단어 뒤집기 2
def solution(string):
    answer = []
    import re
    wordList = re.findall('<[a-zA-Z0-9 ]+>|[a-zA-Z0-9]+| ', string)
    for word in wordList:
        if word[0] == "<" or word == ' ':
            answer.append(word)
        else:
            answer.append(word[::-1])
    return ''.join(answer)

print(solution("baekjoon online judge")) # noojkeab enilno egduj
print(solution("<open>tag<close>")) # <open>gat<close>
print(solution("<ab cd>ef gh<ij kl>")) # <ab cd>fe hg<ij kl>
print(solution("one1 two2 three3 4fourr 5five 6six")) # 1eno 2owt 3eerht rruof4 evif5 xis6
# <int><max>7463847412<long long><max>7085774586302733229
print(solution("<int><max>2147483647<long long><max>9223372036854775807"))
# <problem>31471<is hardest>melborp reve<end>
print(solution("<problem>17413<is hardest>problem ever<end>"))
# <   space   >ecaps ecaps ecaps<    spa   c e>
print(solution("<   space   >space space space<    spa   c e>"))

def solution(string):
    result = ''
    ck = False
    tmp = ''
    for i in string:
        if i == ' ':
            if not ck:
                result += tmp[::-1]+" "
                tmp = ""
            else:
                result += " "
        elif i == '<':
            ck = True
            result += tmp[::-1] + '<'
            tmp = ""
        elif i == '>':
            ck = False
            result += '>'
        else:
            if ck:
                result += i
            else:
                tmp += i
    result += tmp[::-1]
    return result

print(solution("baekjoon online judge")) # noojkeab enilno egduj
print(solution("<open>tag<close>")) # <open>gat<close>
print(solution("<ab cd>ef gh<ij kl>")) # <ab cd>fe hg<ij kl>
print(solution("one1 two2 three3 4fourr 5five 6six")) # 1eno 2owt 3eerht rruof4 evif5 xis6
# <int><max>7463847412<long long><max>7085774586302733229
print(solution("<int><max>2147483647<long long><max>9223372036854775807"))
# <problem>31471<is hardest>melborp reve<end>
print(solution("<problem>17413<is hardest>problem ever<end>"))
# <   space   >ecaps ecaps ecaps<    spa   c e>
print(solution("<   space   >space space space<    spa   c e>"))
