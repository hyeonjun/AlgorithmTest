import sys
input=sys.stdin.readline
n, m = map(int, input().split())

words = [0 for _ in range(n)]
for i in range(n):
    for w in input().strip():  # | -> (1 | 1) = 1, (1 | 0) = 1, (0 | 1) = 1
        words[i] |= 1 << ord(w) - ord('a')  # 각 알파벳 위치 1로 -> 외움 표시

# 26개의 알파벳 여부 - 모두 1로 초기화
# 모음은 잊지 않음
alp = (1 << 26) - 1
for _ in range(m):
    o, x = input().split()
    if o == '1': # 잊는다
        alp &= ~(1 << ord(x) - ord('a'))
    else: # 기억해낸다
        alp |= 1 << ord(x) - ord('a')

    answer = 0
    for word in words:
        if alp & word == word:
            answer += 1
    print(answer)