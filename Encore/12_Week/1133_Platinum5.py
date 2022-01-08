# # # 백트래킹
# # # 문자열의 길이가 n이면서 k-반복X이면서 알파벳 처음 a로 이루어진 단어 중 사전순 맨 처음 것
import sys
def check(s):
    n = len(s)
    dp = [[2 for _ in range(n)] for _ in range(n)]
    result = 2 # 최소 k
    for i in range(n-1): # 인덱스 기준
        for j in range(1, n//2+1): # 길이
            if i+j*2 > n:
                break
            if s[i:i+j] == s[i+j:i+j*2]: # 반복이면
                dp[i+j][j] = dp[i][j] + 1 # 횟수 올림
                result = max(result, dp[i+j][j])
    return result

# 1
def backtracking(string):
    if len(string) == N:
        return string
    for i in range(A):
        words = string + chr(ord('A')+i)
        if check(words) <= K:
            result = backtracking(words)
            if result != -1:
                return result
    return -1
K, N, A = map(int, input().split())
print(backtracking("A"))

# 2
def backtracking():
    if len(answer) == N:
        print(''.join(answer))
        sys.exit(0)
    for i in range(A):
        answer.append(chr(ord('A')+i))
        if check(''.join(answer)) <= K:
            backtracking()
        answer.pop()
    return -1
K, N, A = map(int, input().split())
answer = ['A']
print(backtracking())

# 3
def backtracking():
    global answer
    if check(answer) > K:
        return
    if len(answer) == N:
        print(''.join(answer))
        sys.exit(0)
    for i in range(A):
        answer += chr(ord('A')+i)
        backtracking()
        answer = answer[:-1]
    return -1
K, N, A = map(int, input().split())
answer = 'A'
print(backtracking())
