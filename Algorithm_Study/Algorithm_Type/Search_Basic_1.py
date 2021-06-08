# -*- coding : cp949 -*-
# 문자열에서 중복없이 원하는 단어의 개수 구하기
def solution(string, find):
    import re
    return len(re.findall(find, string))

print(solution("ababababa", "aba")) # 2
print(solution("a a a a a", "a a")) # 2

def solution(string, find):
    i = 0
    result = 0
    while len(string) - i >= len(find):
        if string[i:i+len(find)] == find:
            result += 1
            i += len(find)
        else:
            i += 1
    return result

print(solution("ababababa", "aba")) # 2
print(solution("a a a a a", "a a")) # 2

# ===========================================================================

# N마리의 새
def solution(N):
    answer = 0
    time = 0
    while N > 0:
        time += 1
        if N > time:
            N -= time
        else:
            N -= 1
            time = 1
        answer += 1
    return answer

print(solution(14)) # 7

def solution(N):
    result = 0
    K = 1
    while N != 0:
        if K>N:
            K = 1
        N -= K
        K += 1
        result += 1
    return result

print(solution(14)) # 7

# ===========================================================================

# 베스트셀러
def solution(n, name):
    book = {}
    for i in name:
        if i in book:
            book[i] += 1
        else:
            book[i] = 1
    maxV = max(book.values())
    answer = [i for i in book if book[i] == maxV]

    return sorted(answer)[0]

print(solution(5, ["top", "top", "top", "top", "kimtop"]))
print(solution(5, ["top", "top", "tmp", "kimtop", "kimtop"]))

# ===========================================================================

# 트로피 진열
def solution(trophy):
    def check(array):
        now = array[0]
        result = 1
        for i in range(1, len(array)):
            if now < array[i]:
                result += 1
                now = array[i]
        return result
    l = check(trophy)
    trophy.reverse()
    r = check(trophy)
    return l,r
print(solution([1,2,3,4,5])) # 5,1
# n = int(input())
# array = []
# for _ in range(n):
#     array.append(int(input()))
# l, r = solution(array)
# print("{0}\n{1}".format(l, r))

# ===========================================================================

# 성 지키기
def solution(r, c, castle):
    row, col = [0] * r, [0] * c
    answer = [0,0]
    for i in range(r):
        for j in range(c):
            if castle[i][j] == 'X':
                row[i] += 1
                col[j] += 1
    for i in range(r):
        if row[i] == 0:
            answer[0] += 1
    for i in range(c):
        if col[i] == 0:
            answer[1] += 1
    return max(answer)

# n,m = map(int, input().split())
# array = []
# for _ in range(n):
#     array.append(input())
#
# print(solution(n, m, array))

print(solution(4,4,[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]))
