"""
a n t i c 무조건 배워야하는 글자
"""
# ========================================================
# dfs 백트래킹
# ========================================================
n, k = map(int, input().split())
if k < 5:
    print(0)
elif k == 26:
    print(n)
else:
    answer = 0
    words = [set(input()) for _ in range(n)]

    learn = [False for _ in range(26)]
    for w in list('antic'):
        learn[ord(w)-ord('a')] = True # 배움

    def dfs(idx, cnt):
        global answer
        if cnt == k-5: # 학습할 수 있는 단어를 모두 가르쳤으면
            result = 0
            for word in words:
                flag = True
                for w in word:
                    if not learn[ord(w)-ord('a')]: # 안배웠으면
                        flag = False
                        break
                if flag: # 읽을 수 있으면
                    result += 1
            answer = max(answer, result)
            return

        for i in range(idx, 26):
            if not learn[i]:
                learn[i] = True
                dfs(i, cnt+1)
                learn[i] = False
    dfs(0, 0)
    print(answer)


# ========================================================
# 비트마스킹
# ========================================================
from itertools import combinations
def ord_convert(x):
    return ord(x) - ord('a')

def bit_convert(arr):
    result = 0
    for i in arr:
        result |= (1 << i)
    return result

n, k = map(int, input().split())
word = set([ord_convert(x) for x in ['a', 'n', 't', 'i', 'c']])
base = bit_convert(word)
wordList = [set(map(ord_convert, input())) for _ in range(n)]

wordList_ = [bit_convert(i) for i in wordList]
candidate = set().union(*wordList) - word # 이미 배운 것을 제외하고 고를 수 있는 후보
answer = 0

if k < 5:
    print(0)
else:
    if len(candidate) <= k-5:
        print(n)
    else:
        for c in combinations(candidate, k-5):
            tmp = base
            for i in c:
                tmp |= (1 << i)
            tmp ^= (1 << 26) - 1
            answer = max(answer, sum(1 if tmp & a == 0 else 0 for a in wordList_))
        print(answer)