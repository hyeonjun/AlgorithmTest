"""
연산 1: 뒤에 A 추가
연산 2: 뒤에 B 추가한 후 문자열 뒤집기

1. A...A
 - 연산1 -> 맨 뒤 A 제거

2. A...B
 - 존재할 수 없는 경우의 수

3. B...A
 - 두 연산 모두 가능
 - 연산1 -> 맨 뒤 A 제거
 - 연산2 -> 뒤집고 맨 뒤 B 제거

4. B...B
 - 연산2 -> 뒤집고 맨 뒤 B 제거
"""
S = input()
T = list(input())
answer = 0

# 방법 1
# def dfs(t):
#     global answer
#     if len(S) == len(t):
#         if S == ''.join(t):
#             answer = 1
#         return
#
#     if answer == 1:
#         return
#
#     if t[0] == 'B':
#         t = t[::-1]
#         t.pop()
#         dfs(t)
#         t.append('B')
#         t = t[::-1]
#     if t[-1] == 'A':
#         t.pop()
#         dfs(t)
#         t.append('A')

# 방법 2
def dfs(t):
    global answer
    if len(t) == len(S):
        if S == ''.join(t):
            answer = 1
        return
    if answer == 1:
        return

    if t[0] == 'B':
        dfs(t[:0:-1])
    if t[-1] == 'A':
        dfs(t[:-1])


dfs(T)
print(answer)
