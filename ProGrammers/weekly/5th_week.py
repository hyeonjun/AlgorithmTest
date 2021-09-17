def solution(word):
    dic = []
    alpha = ['A', 'E', 'I', 'O', 'U']

    def words(s):
        if len(s) == 6:
            return
        dic.append(s)
        for i in alpha:
            words(s + i)

    for i in alpha:
        words(i)
    return dic.index(word) + 1

print(solution("AAAAE")) # 6
print(solution("AAAE")) # 10
print(solution("I")) # 1563
print(solution("EIO")) # 1189

def solution(word):
    from itertools import product
    dic = []
    alpha = ['A', 'E', 'I', 'O', 'U']
    for i in range(1, 6):
        dic.extend(list(map(''.join, product(alpha, repeat=i))))
    dic.sort()
    return dic.index(word) +1

print(solution("AAAAE")) # 6
print(solution("AAAE")) # 10
print(solution("I")) # 1563
print(solution("EIO")) # 1189

